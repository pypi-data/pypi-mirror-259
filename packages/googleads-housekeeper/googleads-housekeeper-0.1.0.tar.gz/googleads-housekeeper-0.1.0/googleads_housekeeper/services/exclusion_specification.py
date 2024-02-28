# Copyright 2022 Google LLC
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
"""Module for building and applying various specification.

ExclusionSpecification holds an expression is checked against a particular
GaarfRow object to verify whether or not this expression is true.
"""
from __future__ import annotations

import itertools
import logging
import re
from collections.abc import Sequence
from dataclasses import asdict

from gaarf.report import GaarfReport
from gaarf.report import GaarfRow

from googleads_housekeeper.services.enums import ExclusionTypeEnum
from googleads_housekeeper.services.enums import PlacementTypeEnum
from googleads_housekeeper.services.external_parsers.base_parser import BaseParser
from googleads_housekeeper.services.external_parsers.base_parser import NullParser
from googleads_housekeeper.services.external_parsers.website_parser import WebSiteParser
from googleads_housekeeper.services.external_parsers.youtube_data_parser import ChannelInfoParser
from googleads_housekeeper.services.external_parsers.youtube_data_parser import VideoInfoParser
from googleads_housekeeper.services.unit_of_work import AbstractUnitOfWork

_PARSEABLE_PLACEMENT_TYPES = ('WEBSITE', 'YOUTUBE_VIDEO', 'YOUTUBE_CHANNEL')


class BaseExclusionSpecification:
    """Base class for holding logic applicable to all specifications.

    Attributes:
        name:
            name of the metric/dimension from Google Ads.
        operator:
            comparator used to evaluate the expression.
        value:
            expected value metric should take.
        exclusion_type:
            type of the parseable entity, depending on it additional data might
            be fetched from the repository.
        parser:
            parser which should be use when entity is not in the repository.
        corresponding_placement_type:
            type of the evaluated placement.
        repository_name:
            repository to get information on parsed entity.
    """

    def __init__(self,
                 expression: str,
                 exclusion_type: ExclusionTypeEnum | None = None,
                 parser: type[BaseParser] = NullParser,
                 placement_type: PlacementTypeEnum | None = None,
                 repository_name: str | None = None):
        """Constructor for the class.

        Args:
            expression: exclusion expression in a form of `name > value`
            exclusion_type: type of the exclusion
            parser: parser for getting data from API and/or DB
        """
        elements = [
            element.strip() for element in expression.split(' ', maxsplit=2)
        ]
        if len(elements) != 3:
            raise ValueError(
                "Incorrect expression, specify in 'name > value' format")
        if elements[1] not in ('>', '>=', '<', '<=', '=', '!=', 'regexp',
                               'contains', 'has_latin_letters'):
            raise ValueError(
                'Incorrect operator for expression, '
                "only '>', '>=', '<', '<=', '=', '!=', 'regexp', 'contains' ",
                "'has_latin_letters' are supported'")

        self.name = elements[0]
        self.operator = '==' if elements[1] == '=' else elements[1]
        self.__raw_value = elements[2].replace("'", '').replace('"', '')
        if self.__raw_value.lower() == 'true':
            self.value = '^[a-zA-Z ]*$'
        elif self.__raw_value.lower() == 'false':
            self.value = '^[^a-zA-Z]*$'
        else:
            self.value = self.__raw_value
        self.exclusion_type = exclusion_type
        self.parser = parser
        self.corresponding_placement_type = placement_type
        self.repository_name = repository_name

    def is_satisfied_by(
            self,
            placement_info: GaarfRow,
            uow: AbstractUnitOfWork | None = None) -> tuple[bool, dict]:
        """Verify whether given entity satisfies stored expression.

        Args:
            placement_info: GaarfRow object that contains entity data.
        Returns:
            Tuple with results of evaluation and all necessary information on
            placement (formatted as a dict).
        """
        placement_as_dict = {}
        with uow:
            if (placement_info.placement_type in _PARSEABLE_PLACEMENT_TYPES and
                    self.exclusion_type != ExclusionTypeEnum.GOOGLE_ADS_INFO):
                if placement := getattr(uow,
                                        self.repository_name).get_by_condition(
                                            'placement',
                                            placement_info.placement):
                    placement = placement[0]
                    placement_as_dict = asdict(placement)
                else:
                    # Haven't found a placement in DB, cannot apply the rule
                    return False, placement_as_dict
            else:
                placement = placement_info
            if not hasattr(placement, self.name):
                raise ValueError(f'{self.name} is not found!')
            if hasattr(placement,
                       'is_processed') and not placement.is_processed:
                logging.debug(
                    'Cannot get internal information on %s placement of type %s',
                    placement_info.placement, placement_info.placement_type)
                return False, placement_as_dict
            if self.operator in ('regexp', 'contains', 'has_latin_letters'):
                return self._check_regexp(placement), placement_as_dict
            return self._eval_expression(placement), placement_as_dict

    def _check_regexp(self, placement: GaarfRow) -> bool:
        if placement_element := getattr(placement, self.name):
            punctuation_regex = re.compile('f[{re.escape(punctuation)}]')
            return bool(
                re.search(fr'{self.value}',
                          punctuation_regex.sub('', placement_element),
                          re.IGNORECASE))
        return False

    def _eval_expression(self, placement):
        try:
            value = float(self.value)
        except ValueError:
            value = self.value
        if isinstance(value, float):
            return eval(
                f'{getattr(placement, self.name)}{self.operator} {value}')
        return getattr(placement, self.name) == value

    def __str__(self):
        return f'{self.exclusion_type.name}:{self.name} {self.operator} {self.value}'

    def __repr__(self):
        return (f'{self.__class__.__name__}'
                f"(exclusion_type='{self.exclusion_type.name}', "
                f"name='{self.name}', "
                f"operator='{self.operator}', value='{self.value}')")

    def __eq__(self, other):
        return (self.exclusion_type, self.name, self.operator,
                self.value) == (other.exclusion_type, other.name,
                                other.operator, other.value)


class AdsExclusionSpecification(BaseExclusionSpecification):
    """Stores Google Ads specific rules."""

    def __init__(self, expression):
        super().__init__(expression,
                         exclusion_type=ExclusionTypeEnum.GOOGLE_ADS_INFO)


class ContentExclusionSpecification(BaseExclusionSpecification):
    """Stores Website specific rules."""

    def __init__(self, expression) -> None:
        super().__init__(expression=expression,
                         exclusion_type=ExclusionTypeEnum.WEBSITE_INFO,
                         parser=WebSiteParser,
                         placement_type=PlacementTypeEnum.WEBSITE,
                         repository_name='website_info')


class YouTubeChannelExclusionSpecification(BaseExclusionSpecification):
    """Stores YouTube Channel specific rules."""

    def __init__(self, expression) -> None:
        super().__init__(expression=expression,
                         exclusion_type=ExclusionTypeEnum.YOUTUBE_CHANNEL_INFO,
                         parser=ChannelInfoParser,
                         placement_type=PlacementTypeEnum.YOUTUBE_CHANNEL,
                         repository_name='youtube_channel_info')


class YouTubeVideoExclusionSpecification(BaseExclusionSpecification):
    """Stores YouTube Video specific rules."""

    def __init__(self, expression) -> None:
        super().__init__(expression=expression,
                         exclusion_type=ExclusionTypeEnum.YOUTUBE_VIDEO_INFO,
                         parser=VideoInfoParser,
                         placement_type=PlacementTypeEnum.YOUTUBE_VIDEO,
                         repository_name='youtube_video_info')


class NullSpecification(BaseExclusionSpecification):
    """Handles unsupported rules."""

    def __init__(self, specification_type, expression):
        super().__init__(type)
        raise ValueError(f'Incorrect type of rule: {specification_type}')


class Specification:
    """Applies specifications to a report.

    Attributes:
        uow: unit of work for performing repository checks.
    """

    def __init__(self, uow: AbstractUnitOfWork | None = None):
        self.uow = uow

    def apply_specifications(self, specifications: Sequence[
        Sequence[BaseExclusionSpecification]],
                             placements: GaarfReport) -> GaarfReport | None:
        """Get placements that satisfy exclusion specifications."""
        to_be_excluded_placements = []
        with self.uow as uow:
            for placement in placements:
                is_allowlisted = False
                reason, matching_placement = self.satisfies(
                    specifications, placement)
                if reason:
                    reason_str = ','.join(list(itertools.chain(*reason)))
                    if uow.allowlisting.get_by_conditions({
                            'name': placement.placement,
                            'type': placement.placement_type,
                            'account_id': placement.customer_id
                    }):
                        is_allowlisted = True
                    to_be_excluded_placements.append(
                        placement.data +
                        [reason_str, matching_placement, is_allowlisted])
        if to_be_excluded_placements:
            return GaarfReport(results=to_be_excluded_placements,
                               column_names=placements.column_names +
                               ['reason', 'extra_info', 'allowlist'])
        return None

    def satisfies(self, specs: Sequence[Sequence[BaseExclusionSpecification]],
                  placement: GaarfRow) -> tuple[list[str], dict]:
        """Verity whether a single entity satisfies the specifications.

        Args:
            specs: specifications that needs to be satisfied.
            placement: GaarfRow object with placement data.
        Returns:
            Tuple with list of rules that placement satisfies and
            placement itself.
        """
        rules_satisfied: list[str] = []
        placement_satisfied: dict = {}
        for spec_entry in specs:
            spec_satisfied: list[str] = []
            for spec in spec_entry:
                if spec.exclusion_type != ExclusionTypeEnum.GOOGLE_ADS_INFO:
                    formatted_exclusion_type = spec.exclusion_type.name.replace(
                        '_INFO', '')
                    if formatted_exclusion_type != placement.placement_type:
                        continue
                is_satisfied, placement_satisfied = spec.is_satisfied_by(
                    placement, self.uow)
                if is_satisfied:
                    spec_satisfied.append(str(spec))
                    continue
            if len(spec_satisfied) == len(spec_entry):
                rules_satisfied.append(spec_satisfied)
        return rules_satisfied, placement_satisfied


def create_exclusion_specification(
        specification_type: str, condition: str) -> BaseExclusionSpecification:
    """Builds concrete specification class based on type.

    Args:
        specification_type: type of desired specification.
        condition: expression to use for building the specification.

    Returns:
        Any subclass of instance of BaseExclusionSpecification.
    """
    if specification_type == 'GOOGLE_ADS_INFO':
        return AdsExclusionSpecification(condition)
    if specification_type == 'WEBSITE_INFO':
        return ContentExclusionSpecification(condition)
    if specification_type == 'YOUTUBE_CHANNEL_INFO':
        return YouTubeChannelExclusionSpecification(condition)
    if specification_type == 'YOUTUBE_VIDEO_INFO':
        return YouTubeVideoExclusionSpecification(condition)
    return NullSpecification(specification_type, condition)
