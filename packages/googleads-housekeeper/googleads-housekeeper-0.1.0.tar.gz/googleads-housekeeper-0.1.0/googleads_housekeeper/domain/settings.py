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
"""Entities for configuring the application."""
from __future__ import annotations

import uuid
from dataclasses import dataclass
from dataclasses import field


@dataclass
class Config:
    mcc_id: str
    email_address: str
    always_fetch_youtube_preview_mode: bool = True
    save_to_db: bool = True
    id: str = field(default_factory=lambda: str(uuid.uuid4()))


@dataclass
class CustomerIds:
    mcc_id: str
    account_name: str
    id: str


@dataclass
class MccIds:
    id: str
    account_name: str
