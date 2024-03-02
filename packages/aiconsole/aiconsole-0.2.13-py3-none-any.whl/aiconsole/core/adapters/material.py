# The AIConsole Project
#
# Copyright 2023 10Clouds
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from enum import Enum

from pydantic import BaseModel

from aiconsole.core.assets.types import Asset


class AssetType(str):
    pass


"""
Prototye Work in Progress

Ideation of how an adapter for https://github.com/10clouds/aiconsole/issues/712

This, and execution modes should be assets
"""


class AssetLocationLevel(str, Enum):
    AICONSOLE_CORE = "aiconsole"
    WORKSPACE_DIR = "workspace"
    PROJECT_DIR = "project"


class AssetLocation(BaseModel):
    level: AssetLocationLevel
    id: str
    private: bool = False


class Adapter(Asset):
    id: str
    name: str
    version: str = "0.0.1"

    async def fetch_objects(self, type: AssetType) -> list[Asset]:
        return []

    async def fetch_object(self, type: AssetType, id: str) -> Asset:
        raise NotImplementedError

    async def save_obj(self, obj: Asset):
        raise NotImplementedError
