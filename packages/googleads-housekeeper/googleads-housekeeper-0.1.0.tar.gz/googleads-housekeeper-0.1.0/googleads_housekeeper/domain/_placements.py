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
"""Contains classes and function to work with Placements from Google Ads API."""
from __future__ import annotations

from datetime import datetime
from datetime import timedelta

import numpy as np
from gaarf.base_query import BaseQuery
from gaarf.report import GaarfReport

from googleads_housekeeper.services.enums import CampaignTypeEnum
from googleads_housekeeper.services.enums import ExclusionLevelEnum
from googleads_housekeeper.services.enums import PlacementTypeEnum


class Placements(BaseQuery):
    """Contains placement meta information and it's performance.

    Placements is a wrapper on BaseQuery that builds GAQL query (located in
    `query_text` attribute) based on provided and validated inputs.
    """

    _today = datetime.today()
    _start_date = _today - timedelta(days=7)
    _end_date = _today - timedelta(days=1)
    _campaign_types = {c.name for c in CampaignTypeEnum}
    _placement_types = {p.name for p in PlacementTypeEnum}
    _non_excludable_placements = ('youtube.com', 'mail.google.com',
                                  'adsenseformobileapps.com')
    _non_supported_campaign_types = ('MULTI_CHANNEL',)

    def __init__(self,
                 placement_types: tuple[str, ...] | None = None,
                 campaign_types: tuple[str, ...] | None = None,
                 placement_level_granularity: str = 'group_placement_view',
                 start_date: str = _start_date.strftime('%Y-%m-%d'),
                 end_date: str = _end_date.strftime('%Y-%m-%d'),
                 clicks: int = 0,
                 cost: int = 0,
                 impressions: int = 0,
                 ctr: float = 1.0):
        """Constructor for the class.

        Args:
            placement_types: List of campaign types that need to be fetched.
            placement_types: List of placement types that need to be fetched
                for exclusion.
            start_date: Start_date of the period.
            end_date: Start_date of the period.
            clicks: Number of clicks for the period.
            impressions: Number of impressions for the period.
            cost: Cost for the period.
            impressions: Impressions for the period.
            ctr: Average CTR for the period.
        """
        if campaign_types:
            if isinstance(campaign_types, str):
                campaign_types = tuple(campaign_types.split(','))
            if (wrong_types :=
                    set(campaign_types).difference(self._campaign_types)):
                raise ValueError('Wrong campaign type(s): ',
                                 ', '.join(wrong_types))
            self.campaign_types = '","'.join(campaign_types)
        else:
            self.campaign_types = '","'.join(self._campaign_types)
        if placement_types:
            if isinstance(placement_types, str):
                placement_types = tuple(placement_types.split(','))
            if (wrong_types :=
                    set(placement_types).difference(self._placement_types)):
                raise ValueError('Wrong placement(s): ', ', '.join(wrong_types))
            self.placement_types = '","'.join(placement_types)
        else:
            self.placement_types = '","'.join(self._placement_types)

        if placement_level_granularity not in ('detail_placement_view',
                                               'group_placement_view'):
            raise ValueError(
                "Only 'detail_placement_view' or 'group_placement_view' "
                'can be specified!')
        self.placement_level_granularity = placement_level_granularity

        self.validate_dates(start_date, end_date)
        self.start_date = start_date
        self.end_date = end_date
        self.non_excludable_placements = '","'.join(
            self._non_excludable_placements)
        self.parent_url = ('group_placement_target_url'
                           if self.placement_level_granularity
                           == 'detail_placement_view' else 'target_url')
        self.query_text = f"""
        SELECT
            customer.descriptive_name AS account_name,
            customer.id AS customer_id,
            campaign.id AS campaign_id,
            campaign.name AS campaign_name,
            campaign.advertising_channel_type AS campaign_type,
            ad_group.id AS ad_group_id,
            ad_group.name AS ad_group_name,
            {self.placement_level_granularity}.{self.parent_url} AS base_url,
            {self.placement_level_granularity}.target_url AS url,
            {self.placement_level_granularity}.placement AS placement,
            {self.placement_level_granularity}.placement_type AS placement_type,
            {self.placement_level_granularity}.resource_name AS resource_name,
            {self.placement_level_granularity}.display_name AS name,
            {self.placement_level_granularity}.resource_name~0 AS criterion_id,
            metrics.clicks AS clicks,
            metrics.impressions AS impressions,
            metrics.cost_micros / 1e6 AS cost,
            metrics.conversions AS conversions,
            metrics.video_views AS video_views,
            metrics.interactions AS interactions,
            metrics.all_conversions AS all_conversions,
            metrics.all_conversions_value AS all_conversions_value,
            metrics.view_through_conversions AS view_through_conversions,
            metrics.conversions_value AS conversions_value
        FROM {self.placement_level_granularity}
        WHERE segments.date >= "{self.start_date}"
            AND segments.date <= "{self.end_date}"
            AND {self.placement_level_granularity}.placement_type IN
                ("{self.placement_types}")
            AND {self.placement_level_granularity}.target_url NOT IN
                ("{self.non_excludable_placements}")
            AND campaign.advertising_channel_type IN ("{self.campaign_types}")
            AND metrics.clicks >= {clicks}
            AND metrics.impressions > {impressions}
            AND metrics.ctr < {ctr}
            AND metrics.cost_micros >= {int(cost*1e6)}
        """

    def validate_dates(self, start_date: str, end_date: str) -> None:
        """Checks whether provides start and end dates are valid."""
        if not self.is_valid_date(start_date):
            raise ValueError(f'Invalid start_date: {start_date}')

        if not self.is_valid_date(end_date):
            raise ValueError(f'Invalid end_date: {end_date}')

        if datetime.strptime(start_date, '%Y-%m-%d') > datetime.strptime(
                end_date, '%Y-%m-%d'):
            raise ValueError('start_date cannot be greater than end_date: '
                             f'{start_date} > {end_date}')

    def is_valid_date(self, date_string: str) -> bool:
        try:
            datetime.strptime(date_string, '%Y-%m-%d')
            return True
        except ValueError:
            return False


class PlacementsConversionSplit(Placements):
    """Placement conversion performance by each conversion name."""
    _today = datetime.today()
    _start_date = _today - timedelta(days=7)
    _end_date = _today - timedelta(days=1)

    def __init__(
        self,
        placement_types: tuple[str, ...] | None = None,
        campaign_types: tuple[str, ...] | None = None,
        placement_level_granularity: str = 'group_placement_view',
        start_date: str = _start_date.strftime('%Y-%m-%d'),
        end_date: str = _end_date.strftime('%Y-%m-%d')
    ) -> None:
        super().__init__(placement_types, campaign_types,
                         placement_level_granularity, start_date, end_date)
        self.query_text = f"""
        SELECT
            campaign.advertising_channel_type AS campaign_type,
            ad_group.id AS ad_group_id,
            segments.conversion_action_name AS conversion_name,
            {self.placement_level_granularity}.placement AS placement,
            metrics.conversions AS conversions,
            metrics.all_conversions AS all_conversions
        FROM {self.placement_level_granularity}
        WHERE segments.date >= "{self.start_date}"
            AND segments.date <= "{self.end_date}"
            AND {self.placement_level_granularity}.placement_type IN
                ("{self.placement_types}")
            AND {self.placement_level_granularity}.target_url NOT IN
                ("{self.non_excludable_placements}")
            AND campaign.advertising_channel_type IN ("{self.campaign_types}")
        """


def aggregate_placements(
        placements: GaarfReport,
        exclusion_level: str | ExclusionLevelEnum,
        perform_relative_aggregations: bool = True) -> GaarfReport:
    """Aggregates placements to a desired exclusion_level.

    By default Placements report returned on Ad Group level, however exclusion
    can be performed on Campaign, Account and MCC level. By aggregating report
    to a desired level exclusion specification can be property applied to
    identify placements that should be excluded.

    Args:
        placements:
            Report with placement related metrics.
        exclusion_level:
            Desired level of aggregation.
        perform_relative_aggregations:
            Whether or not calculate relative metrics (CTR, CPC, etc.)
    Returns:
        Updated report aggregated to desired exclusion level.
    """
    if not isinstance(exclusion_level, ExclusionLevelEnum):
        exclusion_level = getattr(ExclusionLevelEnum, exclusion_level)
    base_groupby = [
        'placement', 'placement_type', 'name', 'criterion_id', 'url'
    ]
    aggregation_dict = dict.fromkeys([
        'clicks',
        'impressions',
        'cost',
        'conversions',
        'video_views',
        'interactions',
        'all_conversions',
        'view_through_conversions',
    ], 'sum')
    relative_aggregations_dict = {
        'ctr': ['clicks', 'impressions'],
        'avg_cpc': ['cost', 'clicks'],
        'avg_cpm': ['cost', 'impressions'],
        'avg_cpv': ['cost', 'video_views'],
        'video_view_rate': ['video_views', 'impressions'],
        'interaction_rate': ['interactions', 'clicks'],
        'conversions_from_interactions_rate': ['conversions', 'interactions'],
        'cost_per_conversion': ['cost', 'conversions'],
        'cost_per_all_conversion': ['cost', 'all_conversions'],
        'all_conversion_rate': ['all_conversions', 'interactions'],
        'all_conversions_from_interactions_rate': [
            'all_conversions', 'interactions'
        ],
    }
    if 'conversion_name' in placements.column_names:
        base_groupby = base_groupby + ['conversion_name']
        aggregation_dict.update(
            dict.fromkeys(['conversions_', 'all_conversions_'], 'sum'))
        relative_aggregations_dict.update({
            'cost_per_conversion_': ['cost', 'conversions_'],
            'cost_per_all_conversion_': ['cost', 'all_conversions_']
        })

    if exclusion_level == ExclusionLevelEnum.ACCOUNT:
        aggregation_groupby = ['account_name', 'customer_id']
    elif exclusion_level == ExclusionLevelEnum.CAMPAIGN:
        aggregation_groupby = [
            'account_name', 'customer_id', 'campaign_id', 'campaign_name',
            'campaign_type'
        ]
    elif exclusion_level == ExclusionLevelEnum.AD_GROUP:
        aggregation_groupby = [
            'account_name', 'customer_id', 'campaign_id', 'campaign_name',
            'campaign_type', 'ad_group_id', 'ad_group_name'
        ]
    groupby = [
        base for base in base_groupby + aggregation_groupby
        if base in placements.column_names
    ]
    aggregations = {
        key: value
        for key, value in aggregation_dict.items()
        if key in placements.column_names
    }
    aggregated_placements = placements.to_pandas().groupby(
        groupby, as_index=False).agg(aggregations)
    if perform_relative_aggregations:
        for key, [numerator, denominator] in relative_aggregations_dict.items():
            if set([numerator,
                    denominator]).issubset(set(aggregated_placements.columns)):
                aggregated_placements[key] = aggregated_placements[
                    numerator] / aggregated_placements[denominator]
                if key == 'avg_cpm':
                    aggregated_placements[
                        key] = aggregated_placements[key] * 1000
                if key == 'ctr':
                    aggregated_placements[key] = round(
                        aggregated_placements[key], 4)
                else:
                    aggregated_placements[key] = round(
                        aggregated_placements[key], 2)
    aggregated_placements.replace([np.inf, -np.inf], 0, inplace=True)
    return GaarfReport.from_pandas(aggregated_placements)


def join_conversion_split(placements: GaarfReport,
                          placements_by_conversion_name: GaarfReport,
                          conversion_name: str) -> GaarfReport:
    """Joins placements performance data with its conversion split data.

    Args:
        placements:
            Report with placement performance data.
        placements_by_conversion_name:
            Report with placements conversion split data.
        conversion_name:
            Conversion_name(s) that should be used to create a dedicated column
            in joined report.

    Returns:
        New report with extra conversion specific columns.
    """
    placements_by_conversion_name = placements_by_conversion_name.to_pandas()
    final_report_values = []
    for row in placements:
        conversion_row = placements_by_conversion_name.loc[
            (placements_by_conversion_name.ad_group_id == row.ad_group_id)
            & (placements_by_conversion_name.placement == row.placement)]
        data = list(row.data)
        if not (conversions := sum(conversion_row['conversions'].values)):
            conversions = 0.0
        if not (all_conversions := sum(
                conversion_row['all_conversions'].values)):
            all_conversions = 0.0
        data.extend([conversion_name, conversions, all_conversions])
        final_report_values.append(data)
    columns = list(placements.column_names)
    columns.extend(['conversion_name', 'conversions_', 'all_conversions_'])
    return GaarfReport(results=final_report_values, column_names=columns)
