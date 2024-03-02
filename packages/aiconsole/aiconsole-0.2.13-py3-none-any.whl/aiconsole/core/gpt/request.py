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
import logging
from typing import Literal

import tiktoken

from aiconsole.core.gpt.consts import GPTMode
from aiconsole.core.gpt.token_error import TokenError
from aiconsole.core.gpt.tool_definition import ToolDefinition
from aiconsole.core.gpt.types import (
    EnforcedFunctionCall,
    GPTRequestMessage,
    GPTRequestTextMessage,
)
from aiconsole.core.settings.settings import settings
from aiconsole_toolkit.settings.settings_data import REFERENCE_TO_GLOBAL_OPENAI_KEY

_log = logging.getLogger(__name__)

EXTRA_BUFFER_FOR_ENCODING_OVERHEAD = 50


class GPTRequest:
    def __init__(
        self,
        system_message: str,
        messages: list[GPTRequestMessage],
        gpt_mode: GPTMode,
        tools: list[ToolDefinition] = [],
        tool_choice: Literal["none"] | Literal["auto"] | EnforcedFunctionCall | None = None,
        temperature: float = 1,
        presence_penalty: float = 0,
        min_tokens: int = 0,
        preferred_tokens: int = 0,
    ):
        self.system_message = system_message
        self.messages = messages
        self.tools = tools or []
        self.tool_choice = tool_choice
        self.temperature = temperature
        self.gpt_mode = gpt_mode
        self.presence_penalty = presence_penalty
        self.max_tokens = 0

        # Checks if the given prompt can fit within a specified range of token lengths for the specified AI model.

        used_tokens = self.count_tokens() + EXTRA_BUFFER_FOR_ENCODING_OVERHEAD
        available_tokens = self.model_config.max_tokens - used_tokens

        if available_tokens < min_tokens:
            _log.error(
                f"Not enough tokens to perform the modification. Used tokens: {used_tokens},"
                f" available tokens: {available_tokens},"
                f" requested tokens: {self.max_tokens}"
            )

            raise TokenError(
                f"Exceeded the token limit by {min_tokens - available_tokens}, delete/edit some messages or reorganise materials."
            )

        self.max_tokens = min(available_tokens, preferred_tokens)

    def get_messages_dump(self):
        return [message.model_dump(exclude_none=True) for message in self.all_messages]

    @property
    def all_messages(self):
        if self.system_message:
            return [
                GPTRequestTextMessage(role="system", content=self.system_message),
                *self.messages,
            ]
        else:
            return self.messages

    @property
    def llm_settings(self):
        config = self.model_config
        api_key = (
            config.api_key
            if config.api_key != REFERENCE_TO_GLOBAL_OPENAI_KEY
            else settings().unified_settings.openai_api_key
        )
        return {
            "model": config.model,
            **({"api_base": config.api_base} if config.api_base else {}),
            **({"api_key": api_key} if api_key else {}),
            **config.extra,
        }

    @property
    def model_config(self):
        mode_config = settings().unified_settings.gpt_modes.get(self.gpt_mode, None)

        if mode_config is None:
            raise ValueError(
                f"Unknown GPT mode: '{self.gpt_mode}', available modes: {', '.join(settings().unified_settings.gpt_modes.keys())}"
            )

        # if api_key refers to any other setting, use that setting

        for extra in settings().unified_settings.extra:
            if mode_config.api_key == extra:
                mode_config = mode_config.model_copy(update={"api_key": settings().unified_settings.extra[extra]})

        return mode_config

    def count_tokens(self):
        encoding = tiktoken.encoding_for_model(self.model_config.encoding)

        if self.tools:
            functions_tokens = len(encoding.encode(",".join(json.dumps(f.model_dump()) for f in self.tools)))
        else:
            functions_tokens = 0
        return self.count_messages_tokens(encoding) + functions_tokens

    def count_tokens_for_model(self, model):
        encoding = tiktoken.encoding_for_model(self.model_config.encoding)
        return self.count_messages_tokens(encoding)

    def count_messages_tokens(self, encoding):
        messages_str = json.dumps(self.get_messages_dump())
        messages_tokens = len(encoding.encode(messages_str))

        return messages_tokens

    def count_tokens_output(self, message_content: str, message_function_call: dict | None):
        encoding = tiktoken.encoding_for_model(self.model_config.encoding)

        return len(encoding.encode(message_content)) + (
            len(encoding.encode(json.dumps(message_function_call))) if message_function_call else 0
        )

    def validate_request(self):
        """
        Checks if the prompt can be handled by the model
        """

        used_tokens = self.count_tokens()
        model_max_tokens = self.model_config.max_tokens

        if used_tokens - model_max_tokens >= self.max_tokens:
            _log.error(
                f"Not enough tokens to perform the modification. Used tokens: {used_tokens},"
                f" available tokens: {model_max_tokens},"
                f" requested tokens: {self.max_tokens}"
            )
            raise TokenError(
                f"Exceeded the token limit by {self.max_tokens - (used_tokens - model_max_tokens)}, delete/edit some messages or reorganise materials."
            )
