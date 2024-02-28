# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Application handlers."""
from __future__ import annotations

import itertools
import json
import logging
from collections.abc import Sequence
from copy import copy
from dataclasses import asdict
from datetime import datetime
from functools import reduce
from operator import add
from typing import Any

from gaarf.api_clients import GoogleAdsApiClient
from gaarf.query_executor import AdsReportFetcher
from gaarf.report import GaarfReport

from googleads_housekeeper.adapters.notifications import MessagePayload
from googleads_housekeeper.adapters.publisher import BasePublisher
from googleads_housekeeper.adapters.repository import AbstractRepository
from googleads_housekeeper.domain import allowlisting
from googleads_housekeeper.domain import commands
from googleads_housekeeper.domain import events
from googleads_housekeeper.domain import execution
from googleads_housekeeper.domain.placements import aggregate_placements
from googleads_housekeeper.domain.placements import join_conversion_split
from googleads_housekeeper.domain.placements import Placements
from googleads_housekeeper.domain.placements import PlacementsConversionSplit
from googleads_housekeeper.domain.settings import Config
from googleads_housekeeper.domain.settings import CustomerIds
from googleads_housekeeper.domain.settings import MccIds
from googleads_housekeeper.domain.task import Task
from googleads_housekeeper.domain.task import TaskOutput
from googleads_housekeeper.services import unit_of_work
from googleads_housekeeper.services.enums import ExclusionLevelEnum
from googleads_housekeeper.services.enums import ExclusionTypeEnum
from googleads_housekeeper.services.exclusion_service import ExclusionResult
from googleads_housekeeper.services.exclusion_service import PlacementExcluder
from googleads_housekeeper.services.exclusion_specification import (
    BaseExclusionSpecification)
from googleads_housekeeper.services.exclusion_specification import Specification
from googleads_housekeeper.services.exclusion_specification import (
    YouTubeChannelExclusionSpecification)
from googleads_housekeeper.services.rules_parser import RulesParser


def get_mcc_accounts(
        cmd: commands.GetMccIds, uow: unit_of_work.AbstractUnitOfWork,
        ads_api_client: GoogleAdsApiClient) -> list[dict[str, str]]:
    """Fetches and updates mcc accounts in the repository.

    Args:
        cmd: command for getting MccIds.
        uow: unit of work to handle the transaction.
        ads_api_client: client to perform report fetching.
    Returns:
        All mcc accounts available under given root_mcc_id.
    """
    mccs = get_accessible_mccs(ads_api_client, cmd.root_mcc_id)
    result: list[dict[str, str]] = []
    with uow:
        saved_mcc_ids = {int(account.id) for account in uow.mcc_ids.list()}
        fetched_mcc_ids = set(mccs['account_id'].to_list(
            flatten=True, distinct=True))
        new_accounts = fetched_mcc_ids.difference(saved_mcc_ids)
        to_be_removed_accounts = saved_mcc_ids.difference(fetched_mcc_ids)
        for row in mccs:
            row_dict = {'id': row.account_id, 'account_name': row.account_name}
            result.append(row_dict)
            if row.account_id in new_accounts:
                uow.mcc_ids.add(MccIds(**row_dict))
        for account_id in to_be_removed_accounts:
            uow.mcc_ids.delete(account_id)
        uow.commit()
    return result


def get_accessible_mccs(ads_api_client: GoogleAdsApiClient,
                        root_mcc_id: int) -> GaarfReport:
    """Fetches all available mccs under a root_mcc_id.

    Args:
        ads_api_client: client to perform report fetching.
        root_mcc_id: root mmc id for which leaf mccs should be fetched.
    Returns:
        Report with mcc names and ids."""
    query = """
        SELECT
            customer_client.descriptive_name AS account_name,
            customer_client.id AS account_id
        FROM customer_client
        WHERE customer_client.manager = TRUE
        AND customer_client.status = "ENABLED"
        """
    report_fetcher = AdsReportFetcher(api_client=ads_api_client)
    return report_fetcher.fetch(query, root_mcc_id)


def get_customer_ids(
        cmd: commands.GetCustomerIds, uow: unit_of_work.AbstractUnitOfWork,
        ads_api_client: GoogleAdsApiClient) -> list[dict[str, int]]:
    """Fetches accounts under a given mcc_id and update them in the repository.

    Args:
        cmd: command for getting customer ids under a given mcc_id.
        uow: unit of work to handle the transaction.
        ads_api_client: client to perform report fetching.
    Returns:
        All accounts available under given mcc_id.
    """
    customer_ids_query = """
    SELECT
        customer_client.descriptive_name AS account_name,
        customer_client.id AS account_id
    FROM customer_client
    WHERE customer_client.manager = FALSE
    AND customer_client.status = "ENABLED"
    """
    report_fetcher = AdsReportFetcher(api_client=ads_api_client)
    customer_ids = report_fetcher.fetch(
        customer_ids_query, customer_ids=cmd.mcc_id)
    saved_customer_ids = set([
        int(account.id) for account in uow.customer_ids.get_by_conditions(
            {'mcc_id': cmd.mcc_id})
    ])
    fetched_customer_ids = set(customer_ids['account_id'].to_list(
        flatten=True, distinct=True))
    new_accounts = fetched_customer_ids.difference(saved_customer_ids)
    to_be_removed_accounts = saved_customer_ids.difference(fetched_customer_ids)
    result: list[dict[str, int]] = []
    with uow:
        for row in customer_ids:
            result.append({
                'account_name': row.account_name,
                'id': row.account_id
            })
            if row.account_id in new_accounts:
                uow.customer_ids.add(
                    CustomerIds(
                        mcc_id=cmd.mcc_id,
                        account_name=row.account_name,
                        id=str(row.account_id)))
        for account_id in to_be_removed_accounts:
            uow.customer_ids.delete(account_id)
        uow.commit()
    return result


def run_manual_exclusion_task(
        cmd: commands.RunManualExclusion, uow: unit_of_work.AbstractUnitOfWork,
        ads_api_client: GoogleAdsApiClient) -> dict[str, int]:
    with uow:
        placement_excluder = PlacementExcluder(ads_api_client, uow)
        exclusion_result = placement_excluder.exclude_placements(
            to_be_excluded_placements=GaarfReport(
                results=cmd.placements, column_names=cmd.header),
            exclusion_level=ExclusionLevelEnum[cmd.exclusion_level])
    return asdict(exclusion_result)


def task_created(event: events.TaskCreated, publisher: BasePublisher) -> None:
    publisher.publish('_task_created', event)


def task_with_schedule_created(event: events.TaskWithScheduleCreated,
                               publisher: BasePublisher) -> None:
    publisher.publish('task_created', event)


def task_updated(event: events.TaskUpdated, publisher: BasePublisher) -> None:
    publisher.publish('_task_updated', event)


def task_schedule_updated(event: events.TaskScheduleUpdated,
                          publisher: BasePublisher) -> None:
    publisher.publish('task_updated', event)


def task_deleted(event: events.TaskDeleted, publisher: BasePublisher) -> None:
    publisher.publish('_task_deleted', event)


def task_schedule_deleted(event: events.TaskScheduleDeleted,
                          publisher: BasePublisher) -> None:
    publisher.publish('task_deleted', event)


def run_task(cmd: commands.RunTask,
             uow: unit_of_work.AbstractUnitOfWork,
             ads_api_client: GoogleAdsApiClient,
             publisher: BasePublisher | None = None,
             save_to_db: bool = True) -> tuple[dict, MessagePayload | None]:
    n_excluded_placements = 0
    with copy(uow) as uow:
        settings = uow.settings.list()
        task_obj = uow.tasks.get(task_id=cmd.id)
        report_fetcher = AdsReportFetcher(api_client=ads_api_client)
        exclusion_specification = RulesParser().generate_specifications(
            task_obj.exclusion_rule)
        placement_excluder = PlacementExcluder(ads_api_client, uow)
        specification = Specification(uow)
        start_time = datetime.now()
        to_be_excluded_placements = find_placements_for_exclusion(
            task_obj, report_fetcher, specification, exclusion_specification)

        if to_be_excluded_placements and task_obj.output in (
                TaskOutput.EXCLUDE, TaskOutput.EXCLUDE_AND_NOTIFY):
            exclusion_result = placement_excluder.exclude_placements(
                to_be_excluded_placements, task_obj.exclusion_level)

            end_time = datetime.now()
            n_excluded_placements = exclusion_result.excluded_placements
        else:
            exclusion_result = ExclusionResult()
            end_time = datetime.now()
        execution_obj = execution.Execution(
            task=cmd.id,
            start_time=start_time,
            end_time=end_time,
            placements_excluded=n_excluded_placements,
            type=cmd.type)
        uow.executions.add(execution_obj)
        if save_to_db and n_excluded_placements:
            for placement in to_be_excluded_placements:
                if hasattr(placement, 'reason'):
                    exclusion_reason = placement.reason
                else:
                    exclusion_reason = ''
                uow.execution_details.add(
                    execution.ExecutionDetails(
                        execution_id=execution_obj.id,
                        placement=placement.name,
                        placement_type=placement.placement_type,
                        reason=exclusion_reason))
        uow.commit()
        if task_obj.output in (TaskOutput.NOTIFY,
                               TaskOutput.EXCLUDE_AND_NOTIFY):
            publisher.publish('task_run', execution_obj)
            if to_be_excluded_placements:
                message_payload = MessagePayload(
                    task_name=cmd.id,
                    placements_excluded_sample=to_be_excluded_placements[0:10],
                    total_placement_excluded=exclusion_result
                    .excluded_placements,
                    recipient=settings[0].email_address)
            else:
                message_payload = MessagePayload(
                    task_name=cmd.id,
                    placements_excluded_sample=None,
                    total_placement_excluded=0,
                    recipient=settings[0].email_address)
        else:
            message_payload = None
        return asdict(exclusion_result), message_payload


def preview_placements(cmd: commands.PreviewPlacements,
                       uow: unit_of_work.AbstractUnitOfWork,
                       ads_api_client: GoogleAdsApiClient,
                       always_fetch_youtube_preview_mode: bool = True,
                       save_to_db: bool = True) -> dict[str, Any]:
    report_fetcher = AdsReportFetcher(api_client=ads_api_client)
    exclusion_specification = RulesParser().generate_specifications(
        cmd.exclusion_rule)
    task_obj = Task(
        name='',
        exclusion_rule=cmd.exclusion_rule,
        customer_ids=cmd.customer_ids,
        date_range=cmd.date_range,
        from_days_ago=cmd.from_days_ago,
        exclusion_level=cmd.exclusion_level,
        placement_types=cmd.placement_types)
    specification = Specification(uow)
    to_be_excluded_placements = find_placements_for_exclusion(
        task_obj, report_fetcher, specification, exclusion_specification,
        always_fetch_youtube_preview_mode, save_to_db)
    if not to_be_excluded_placements:
        data = {}
    else:
        data = json.loads(
            to_be_excluded_placements.to_pandas().to_json(orient='index'))
    return {
        'data': data,
        'dates': {
            'date_from': task_obj.start_date,
            'date_to': task_obj.end_date
        }
    }


def find_placements_for_exclusion(
        task: Task,
        report_fetcher: AdsReportFetcher,
        specification: Specification,
        exclusion_specification: Sequence[Sequence[BaseExclusionSpecification]]
    | None = None,
        always_fetch_youtube_preview_mode: bool = False,
        save_to_db: bool = True) -> GaarfReport | None:
    runtime_options = RulesParser().define_runtime_options(
        exclusion_specification)
    start_date, end_date = task.get_start_end_date()
    reports: list[GaarfReport] = []
    for account in task.accounts:
        placement_query = Placements(
            placement_types=task.placement_types,
            start_date=start_date,
            end_date=end_date)
        placements = report_fetcher.fetch(placement_query, customer_ids=account)
        if 'YOUTUBE_VIDEO' in task.placement_types:
            youtube_video_placement_query = Placements(
                placement_types=('YOUTUBE_VIDEO',),
                placement_level_granularity='detail_placement_view',
                start_date=start_date,
                end_date=end_date)
            youtube_video_placements = report_fetcher.fetch(
                youtube_video_placement_query, customer_ids=account)
            if youtube_video_placements:
                placements = youtube_video_placements + placements

        if not placements:
            continue
        if runtime_options.is_conversion_query:
            conversion_split_query = PlacementsConversionSplit(
                placement_types=task.placement_types,
                start_date=start_date,
                end_date=end_date)
            placements_by_conversion_name = report_fetcher.fetch(
                conversion_split_query, customer_ids=account)
            if 'YOUTUBE_VIDEO' in task.placement_types:
                youtube_video_conversion_split_query = PlacementsConversionSplit(
                    placement_types=('YOUTUBE_VIDEO',),
                    placement_level_granularity='detail_placement_view',
                    start_date=start_date,
                    end_date=end_date)
                youtube_video_placements_by_conversion_name = report_fetcher.fetch(
                    youtube_video_conversion_split_query, customer_ids=account)
                if youtube_video_placements_by_conversion_name:
                    placements_by_conversion_name = (
                        placements_by_conversion_name +
                        youtube_video_placements_by_conversion_name)
            if not placements_by_conversion_name:
                continue
            placements_by_conversion_name = (
                specification.apply_specifications(
                    [runtime_options.conversion_rules],
                    placements_by_conversion_name))
            placements = join_conversion_split(placements,
                                               placements_by_conversion_name,
                                               runtime_options.conversion_name)
        placements = aggregate_placements(placements, task.exclusion_level)
        if not exclusion_specification:
            with specification.uow as uow:
                for placement in placements:
                    is_allowlisted = False
                    if uow.allowlisting.get_by_conditions({
                            'name': placement.placement,
                            'type': placement.placement_type,
                            'account_id': placement.customer_id
                    }):
                        is_allowlisted = True
                    placement['reason'] = ''
                    placement['allowlist'] = is_allowlisted
                reports.append(placements)
            continue
        for rule in exclusion_specification:
            # Identify all ads and non_ads specifications
            ads_specs = [
                r for r in rule
                if r.exclusion_type == ExclusionTypeEnum.GOOGLE_ADS_INFO
            ]
            non_ads_specs = [
                r for r in rule
                if r.exclusion_type != ExclusionTypeEnum.GOOGLE_ADS_INFO
            ]

            # If we don't have any non_ads specification proceed to applying them
            if not non_ads_specs and always_fetch_youtube_preview_mode:
                non_ads_specs = [
                    YouTubeChannelExclusionSpecification(
                        expression='YOUTUBE_CHANNEL_INFO:title regexp *')
                ]
            if ads_specs and not non_ads_specs:
                continue
            # If we have a mix of ads and non_ads specifications apply ads first
            # and then parse non-ads ones
            if ads_specs and non_ads_specs:
                to_be_parsed_placements = (
                    specification.apply_specifications([ads_specs], placements))
                parse_via_external_parsers(to_be_parsed_placements,
                                           non_ads_specs, specification.uow,
                                           save_to_db)
                if (to_be_excluded_placements :=
                        specification.apply_specifications(
                            exclusion_specification, to_be_parsed_placements)):
                    reports.append(to_be_excluded_placements)
            # If there are only non_ads specification proceed to applying them
            elif not ads_specs and non_ads_specs:
                parse_via_external_parsers(placements, non_ads_specs,
                                           specification.uow, save_to_db)
                if (to_be_excluded_placements :=
                        specification.apply_specifications(
                            exclusion_specification, placements)):
                    reports.append(to_be_excluded_placements)
    if reports:
        return reduce(add, reports)
    return None


def parse_via_external_parsers(
    to_be_parsed_placements: GaarfReport,
    non_ads_specs: Sequence[BaseExclusionSpecification],
    uow: unit_of_work.AbstractUnitOfWork,
    save_to_db: bool = True,
    batch_size: int = 50,
) -> None:
    with uow:
        for non_ads_spec_rule in non_ads_specs:
            _parse_via_external_parser(
                placements=to_be_parsed_placements,
                specification_rule=non_ads_spec_rule,
                uow=uow,
                save_to_db=save_to_db,
                batch_size=batch_size)


def _parse_via_external_parser(placements: GaarfReport,
                               specification_rule: BaseExclusionSpecification,
                               uow: unit_of_work.AbstractUnitOfWork,
                               save_to_db: bool, batch_size: int) -> None:
    repo = getattr(uow, specification_rule.repository_name)
    if not_parsed_placements := _get_not_parsed_placements(
            placements, specification_rule, repo):
        i = 0
        while batch := list(
                itertools.islice(not_parsed_placements, i, i + batch_size)):
            parsed_placements_info = specification_rule.parser().parse(batch)
            i += batch_size
            if save_to_db:
                for parsed_placement in parsed_placements_info:
                    logging.debug('saving placement: %s to db',
                                  parsed_placement)
                    repo.add(parsed_placement)
                uow.commit()


def _get_not_parsed_placements(placements: GaarfReport,
                               specification_rule: BaseExclusionSpecification,
                               repo: AbstractRepository) -> list[str]:
    not_parsed_placements: list[str] = []
    for placement_info in placements:
        if (placement_info.placement_type ==
                specification_rule.corresponding_placement_type.name):

            if not repo.get_by_conditions({
                    'placement': placement_info.placement,
            }):
                not_parsed_placements.append(str(placement_info.placement))
    return not_parsed_placements


def save_task(
    cmd: commands.SaveTask,
    uow: unit_of_work.AbstractUnitOfWork,
) -> str:
    with uow:
        task_id = None
        task_obj = None
        if hasattr(cmd, 'task_id') and cmd.task_id:
            task_id = cmd.task_id
            task_obj = uow.tasks.get(task_id=task_id)
            update_dict = asdict(cmd)
            update_dict.pop('task_id')
            uow.tasks.update(task_obj.id, update_dict)
            uow.commit()
            uow.published_events.append(events.TaskUpdated(cmd.task_id))
            if cmd.schedule and cmd.schedule != task_obj.schedule:
                uow.published_events.append(
                    events.TaskScheduleUpdated(cmd.task_id, cmd.schedule))
            else:
                uow.published_events.append(
                    events.TaskScheduleDeleted(cmd.task_id))
        else:
            task_dict = asdict(cmd)
            task_dict.pop('task_id')
            task_obj = Task(**task_dict)
            uow.tasks.add(task_obj)
            uow.commit()
            task_id = task_obj.id
            uow.published_events.append(events.TaskCreated(task_id))
            if cmd.schedule:
                uow.published_events.append(
                    events.TaskWithScheduleCreated(task_id, cmd.name,
                                                   cmd.schedule))
        task_id = task_obj.id
        return str(task_id)


def delete_task(
    cmd: commands.DeleteTask,
    uow: unit_of_work.AbstractUnitOfWork,
):
    with copy(uow) as uow:
        task_obj = uow.tasks.get(task_id=cmd.task_id)
        if task_obj:
            uow.tasks.update(cmd.task_id, {'status': 'INACTIVE'})
            uow.commit()
            uow.published_events.append(events.TaskDeleted(cmd.task_id))
            uow.published_events.append(events.TaskScheduleDeleted(cmd.task_id))
        else:
            logging.warning('No task with id %d found!', cmd.id)


def save_config(
    cmd: commands.SaveConfig,
    uow: unit_of_work.AbstractUnitOfWork,
):
    with uow:
        if hasattr(cmd, 'id') and cmd.id:
            config_id = cmd.id
            config = uow.settings.get(config_id)
            update_dict = asdict(cmd)
            update_dict.pop('id')
            uow.settings.update(config.id, update_dict)
        else:
            config_dict = asdict(cmd)
            config_dict.pop('id')
            config = Config(**config_dict)
            uow.settings.add(config)
        uow.commit()


def add_to_allowlisting(cmd: commands.AddToAllowlisting,
                        uow: unit_of_work.AbstractUnitOfWork) -> None:
    with uow:
        if not uow.allowlisting.get_by_conditions(asdict(cmd)):
            placement = allowlisting.AllowlistedPlacement(**asdict(cmd))
            uow.allowlisting.add(placement)
            uow.commit()


def remove_from_allowlisting(cmd: commands.RemoveFromAllowlisting,
                             uow: unit_of_work.AbstractUnitOfWork) -> None:
    with uow:
        if allowlisted_placement := uow.allowlisting.get_by_conditions(
                asdict(cmd)):
            uow.allowlisting.delete(allowlisted_placement[0].id)
            uow.commit()


def save_channel_info(cmd: commands.SaveChannelInfo,
                      uow: unit_of_work.AbstractUnitOfWork) -> None:
    with uow:
        uow.youtube_channel_info.add(cmd.channel_info)
        uow.commit()


def save_video_info(cmd: commands.SaveChannelInfo,
                    uow: unit_of_work.AbstractUnitOfWork) -> None:
    with uow:
        uow.youtube_video_info.add(cmd.video_info)
        uow.commit()


def save_website_info(cmd: commands.SaveChannelInfo,
                      uow: unit_of_work.AbstractUnitOfWork) -> None:
    with uow:
        uow.website_info.add(cmd.website_info)
        uow.commit()


EVENT_HANDLERS = {
    events.TaskWithScheduleCreated: [task_with_schedule_created],
    events.TaskScheduleUpdated: [task_schedule_updated],
    events.TaskScheduleDeleted: [task_schedule_deleted],
    events.TaskCreated: [task_created],
    events.TaskUpdated: [task_updated],
    events.TaskDeleted: [task_deleted]
}

COMMAND_HANDLERS = {
    commands.RunTask: run_task,
    commands.SaveTask: save_task,
    commands.DeleteTask: delete_task,
    commands.RunManualExclusion: run_manual_exclusion_task,
    commands.PreviewPlacements: preview_placements,
    commands.SaveConfig: save_config,
    commands.GetCustomerIds: get_customer_ids,
    commands.GetMccIds: get_mcc_accounts,
    commands.AddToAllowlisting: add_to_allowlisting,
    commands.RemoveFromAllowlisting: remove_from_allowlisting,
    commands.SaveChannelInfo: save_channel_info,
    commands.SaveVideoInfo: save_video_info,
    commands.SaveWebsiteInfo: save_website_info,
}
