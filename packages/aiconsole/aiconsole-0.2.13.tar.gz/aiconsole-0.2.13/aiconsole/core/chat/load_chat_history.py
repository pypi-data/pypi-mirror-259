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
import uuid
from datetime import datetime
from pathlib import Path

import aiofiles
import aiofiles.os as async_os

from aiconsole.core.assets.types import AssetLocation
from aiconsole.core.chat.types import AICChat
from aiconsole.core.project.paths import get_history_directory


async def load_chat_history(id: str, project_path: Path | None = None) -> AICChat:
    if id == "new":
        raise ValueError("Cannot load chat with id 'new'")

    history_directory = get_history_directory(project_path)
    file_path = history_directory / f"{id}.json"

    if await async_os.path.exists(file_path):
        async with aiofiles.open(file_path, mode="r", encoding="utf8", errors="replace") as f:
            data = json.loads(await f.read())

            # Convert old format
            if "message_groups" not in data or not data["message_groups"]:
                data["message_groups"] = []

                if "messages" in data and data["messages"]:
                    for message in data["messages"]:
                        data["message_groups"].append(
                            {
                                "id": message["id"] if "id" in message else uuid.uuid4().hex,
                                "role": message["role"] if "role" in message else "",
                                "task": message["task"] if "task" in message and message["task"] else "",
                                "agent_id": message["agent_id"] if "agent_id" in message else "",
                                "materials_ids": (
                                    message["materials_ids"]
                                    if "materials_ids" in message and message["materials_ids"]
                                    else []
                                ),
                                "messages": [
                                    {
                                        "id": message["id"] if "id" in message else uuid.uuid4().hex,
                                        "timestamp": message["timestamp"] if "timestamp" in message else "",
                                        "content": message["content"] if "content" in message else "",
                                    }
                                ],
                            }
                        )
                    del data["messages"]

            # Add tool_calls to each message
            for group in data["message_groups"]:
                if "messages" in group and group["messages"]:
                    for msg in group["messages"]:
                        if "tool_calls" not in msg:
                            msg["tool_calls"] = []

            # For all tool calls without headline add an empty headline
            for group in data["message_groups"]:
                if "messages" in group and group["messages"]:
                    for msg in group["messages"]:
                        if "tool_calls" in msg and msg["tool_calls"]:
                            for tool_call in msg["tool_calls"]:
                                if "headline" not in tool_call:
                                    tool_call["headline"] = ""

            # For each tool with "shell" language change it to "python"
            for group in data["message_groups"]:
                if "messages" in group and group["messages"]:
                    for msg in group["messages"]:
                        if "tool_calls" in msg and msg["tool_calls"]:
                            for tool_call in msg["tool_calls"]:
                                if "language" in tool_call and tool_call["language"] == "shell":
                                    tool_call["language"] = "python"

            # For each tool call add "type" field with default "function" value
            for group in data["message_groups"]:
                if "messages" in group and group["messages"]:
                    for msg in group["messages"]:
                        if "tool_calls" in msg and msg["tool_calls"]:
                            for tool_call in msg["tool_calls"]:
                                if "type" not in tool_call:
                                    tool_call["type"] = "function"

            # For each agent_id change it to actor_id
            for group in data["message_groups"]:
                if "agent_id" in group:
                    group["actor_id"] = {
                        "type": "user" if group["agent_id"] == "user" else "agent",
                        "id": group["agent_id"],
                    }
                    del group["agent_id"]

            # Add "analysis" to each message group
            for group in data["message_groups"]:
                if "analysis" not in group:
                    group["analysis"] = ""

            def extract_default_headline():
                for group in data["message_groups"]:
                    if "messages" in group and group["messages"]:
                        for msg in group["messages"]:
                            return msg.get("content")

            if "name" not in data or not data["name"]:
                if "headline" in data and data["headline"]:
                    data["name"] = data["headline"]
                elif "title" in data and data["title"]:
                    data["name"] = data["title"]
                else:
                    data["name"] = extract_default_headline() or "New Chat"

            if "title_edited" not in data or not data["title_edited"]:
                data["title_edited"] = False
                data["name"] = extract_default_headline() or "New Chat"

            if "id" in data:
                del data["id"]

            if "last_modified" in data:
                del data["last_modified"]

            if "usage_examples" not in data:
                data["usage_examples"] = []

            if "usage" not in data:
                data["usage"] = ""

            if "defined_in" not in data:
                data["defined_in"] = AssetLocation.PROJECT_DIR

            if "override" not in data:
                data["override"] = False

            stat = await async_os.stat(file_path)
            last_modified = datetime.fromtimestamp(stat.st_mtime)

            return AICChat(
                id=id,
                last_modified=last_modified,
                **data,
            )
    else:
        return AICChat(
            id=id,
            name="New Chat",
            usage="",
            usage_examples=[],
            defined_in=AssetLocation.PROJECT_DIR,
            title_edited=False,
            last_modified=datetime.now(),
            message_groups=[],
            override=False,
        )
