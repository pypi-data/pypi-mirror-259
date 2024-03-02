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

from aiconsole.core.chat.types import AICChat, AICMessage, AICMessageGroup
from aiconsole.core.gpt.types import (
    GPTFunctionCall,
    GPTRequestMessage,
    GPTRequestTextMessage,
    GPTRequestToolMessage,
    GPTToolCall,
)


def convert_message(group: AICMessageGroup, message: AICMessage) -> list[GPTRequestMessage]:
    tool_calls = [
        GPTToolCall(
            id=tool_call.id,
            function=GPTFunctionCall(
                name=tool_call.language + "_tool" if tool_call.language else "python_tool",
                arguments=json.dumps(
                    {
                        "code": tool_call.code,
                    }
                ),
            ),
        )
        for tool_call in message.tool_calls
    ]

    result: list[GPTRequestMessage] = [
        GPTRequestTextMessage(
            role=group.role,
            content=message.content,
            name=group.actor_id.id if group.actor_id.type == "agent" else None,
            tool_calls=tool_calls or None,
        )
    ]

    for tool_call in message.tool_calls:
        tool_call_id = tool_call.id

        content = tool_call.output

        if content is None:
            result.append(
                GPTRequestToolMessage(
                    tool_call_id=tool_call_id,
                    content="Running...",
                )
            )
        else:
            if content == "":
                content = "No output"

            result.append(GPTRequestToolMessage(tool_call_id=tool_call_id, content=content))

    return result


def convert_messages(chat: AICChat) -> list[GPTRequestMessage]:
    last_system_message = None

    messages: list[GPTRequestMessage] = []

    for message_group in chat.message_groups:
        is_last_group = message_group == chat.message_groups[-1]
        if message_group.task:
            # Augment the messages with system messages with meta data about which agent is speaking and what materials were available
            system_message = f"""
As a director I have assigned you ({message_group.actor_id.id}) and given you access to the following materials text: {", ".join(message_group.materials_ids) if message_group.materials_ids else "None"}.
""".strip()

            # Only provide a task for last message
            if is_last_group:
                system_message += "\n\nYour job: " + message_group.task

            if last_system_message != system_message:
                messages.append(
                    GPTRequestTextMessage(
                        role="system",
                        name="director",
                        content=system_message,
                    )
                )
                last_system_message = system_message

        for message in message_group.messages:
            messages.extend(convert_message(message_group, message))

        if is_last_group:
            break

    return messages
