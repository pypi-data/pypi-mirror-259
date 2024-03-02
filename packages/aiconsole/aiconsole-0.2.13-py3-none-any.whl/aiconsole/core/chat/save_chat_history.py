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
import json

import aiofiles
import aiofiles.os as async_os

from aiconsole.core.chat.types import AICChat
from aiconsole.core.project.paths import get_history_directory


async def save_chat_history(chat: AICChat, scope: str = "default"):
    history_directory = get_history_directory()
    file_path = history_directory / f"{chat.id}.json"

    new_content = chat.model_dump(exclude={"id", "last_modified"})

    if len(chat.message_groups) == 0 and chat.chat_options.is_default():
        if await async_os.path.exists(file_path):
            await async_os.remove(file_path)
    else:
        await async_os.makedirs(history_directory, exist_ok=True)

        # check if file exists and contents are the same
        if await async_os.path.exists(file_path):
            async with aiofiles.open(file_path, "r", encoding="utf8", errors="replace") as f:
                old_content = json.loads(await f.read())
                if scope == "chat_options" and (
                    "chat_options" not in old_content or old_content["chat_options"] != new_content["chat_options"]
                ):
                    old_content["chat_options"] = new_content["chat_options"]
                    new_content = old_content
                elif scope == "message_groups" and old_content["message_groups"] != new_content["message_groups"]:
                    old_content["message_groups"] = new_content["message_groups"]
                    new_content = old_content
                elif scope == "name" and ("name" not in old_content or old_content["name"] != new_content["name"]):
                    old_content["name"] = new_content["name"]
                    old_content["title_edited"] = True
                    new_content = old_content
                else:
                    return  # contents are the same, no need to write to file

        # write new content to file
        async with aiofiles.open(file_path, "w", encoding="utf8", errors="replace") as f:
            await f.write(json.dumps(new_content))
