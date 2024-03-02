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

from send2trash import send2trash

from aiconsole.core.assets.types import AssetType
from aiconsole.core.project.paths import get_project_assets_directory


def delete_asset_from_fs(asset_type: AssetType, id):
    """
    Delete a specific agent. Need to delete the agent file and the agent avatar file.
    """

    if asset_type == AssetType.AGENT:
        extensions = [".toml", ".jpeg", ".jpg", ".png", ".gif", ".SVG"]
    elif asset_type == AssetType.CHAT:
        extensions = [".json"]
    elif asset_type == AssetType.MATERIAL:
        extensions = [".toml"]

    # check if the file exists in project directory
    for extension in extensions:
        asset_file_path = get_project_assets_directory(asset_type) / f"{id}{extension}"
        if asset_file_path.exists():
            send2trash(asset_file_path)
            # return
    # raise KeyError(f"{asset_type} with ID {id} not found")
