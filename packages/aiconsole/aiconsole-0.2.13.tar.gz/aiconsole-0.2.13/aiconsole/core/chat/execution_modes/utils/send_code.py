import logging
from typing import cast

from aiconsole.core.chat.chat_mutations import (
    AppendToCodeToolCallMutation,
    AppendToHeadlineToolCallMutation,
    CreateToolCallMutation,
    SetCodeToolCallMutation,
    SetHeadlineToolCallMutation,
    SetIsStreamingToolCallMutation,
    SetLanguageToolCallMutation,
)
from aiconsole.core.chat.chat_mutator import ChatMutator
from aiconsole.core.code_running.code_interpreters.language import LanguageStr
from aiconsole.core.code_running.code_interpreters.language_map import language_map
from aiconsole.core.gpt.partial import GPTPartialToolsCall

_log = logging.getLogger(__name__)


def tool_name_to_language(name: str) -> str:
    if name.endswith("_tool"):
        return name[:-5]

    raise Exception(f"Unable to convert name {name} to language")


async def send_code(
    tool_calls: list[GPTPartialToolsCall],
    chat_mutator: ChatMutator,
    tools_requiring_closing_parenthesis,
    message_id,
    language_classes: list[type],
):
    for index, tool_call in enumerate(tool_calls):
        default_language = LanguageStr(tool_name_to_language(language_classes[0].__name__))

        # All tool calls with lower indexes are finished
        prev_tool = tool_calls[index - 1] if index > 0 else None
        if prev_tool and prev_tool.id in tools_requiring_closing_parenthesis:
            await chat_mutator.mutate(
                AppendToCodeToolCallMutation(
                    tool_call_id=prev_tool.id,
                    code_delta=")",
                )
            )

            tools_requiring_closing_parenthesis.remove(prev_tool.id)

        if prev_tool:
            tool_call_location = chat_mutator.chat.get_tool_call_location(prev_tool.id)
            if tool_call_location and tool_call_location.tool_call.is_streaming:
                await chat_mutator.mutate(
                    SetIsStreamingToolCallMutation(
                        tool_call_id=prev_tool.id,
                        is_streaming=False,
                    )
                )

        tool_call_info = chat_mutator.chat.get_tool_call_location(tool_call.id)

        if not tool_call_info:
            await chat_mutator.mutate(
                CreateToolCallMutation(
                    message_id=message_id,
                    tool_call_id=tool_call.id,
                    code="",
                    headline="",
                    language=None,
                    output=None,
                    is_streaming=True,
                    is_executing=False,
                    is_successful=False,
                )
            )

            tool_call_info = chat_mutator.chat.get_tool_call_location(tool_call.id)

            if not tool_call_info:
                raise Exception(f"Tool call {tool_call.id} should have been created")

        tool_call_data = tool_call_info.tool_call

        if not tool_call_data:
            raise Exception(f"Tool call {tool_call.id} not found")

        async def send_language_if_needed(lang: LanguageStr):
            if tool_call_data.language is None:
                await chat_mutator.mutate(
                    SetLanguageToolCallMutation(
                        tool_call_id=tool_call.id,
                        language=lang,
                    )
                )

        async def send_headline_delta_for_headline(headline: str):
            if not headline.startswith(tool_call_data.headline):
                _log.warning(f"Reseting headline to: {headline}")
                await chat_mutator.mutate(
                    SetHeadlineToolCallMutation(
                        tool_call_id=tool_call.id,
                        headline=headline,
                    )
                )
            else:
                start_index = len(tool_call_data.headline)
                headline_delta = headline[start_index:]

                if headline_delta:
                    await chat_mutator.mutate(
                        AppendToHeadlineToolCallMutation(
                            tool_call_id=tool_call.id,
                            headline_delta=headline_delta,
                        )
                    )

        async def send_code_delta_for_code(code: str):
            if not code.startswith(tool_call_data.code):
                _log.warning(f"Reseting code, code={repr(code)} original={repr(tool_call_data.code)}")
                await chat_mutator.mutate(
                    SetCodeToolCallMutation(
                        tool_call_id=tool_call.id,
                        code=code,
                    )
                )
            else:
                start_index = len(tool_call_data.code)
                code_delta = code[start_index:]

                if code_delta:
                    await chat_mutator.mutate(
                        AppendToCodeToolCallMutation(
                            tool_call_id=tool_call.id,
                            code_delta=code_delta,
                        )
                    )

        if tool_call.type == "function":
            function_call = tool_call.function

            if not function_call.arguments:
                continue

            if function_call.name in [language_cls.__name__ for language_cls in language_classes]:
                # Languge is in the name of the function call

                languages = language_map.keys()

                if tool_call_data.language is None and function_call.name in languages:
                    await send_language_if_needed(cast(LanguageStr, function_call.name))

                code = None
                headline = None

                if function_call.arguments_dict:
                    code = function_call.arguments_dict.get("code", None)
                    headline = function_call.arguments_dict.get("headline", None)
                else:
                    # Sometimes we don't have a dict, but it's still a json string

                    if not function_call.arguments.startswith("{"):
                        code = function_call.arguments

                if code:
                    await send_language_if_needed(default_language)
                    await send_code_delta_for_code(code)

                if headline:
                    await send_headline_delta_for_headline(headline)
            else:
                # We have a direct function call, without specifying the language

                await send_language_if_needed(default_language)

                if function_call.arguments_dict:
                    # ok we have a dict, those are probably arguments and the name of the function call is the name of the function

                    arguments_materialised = [
                        f"{key}={repr(value)}" for key, value in function_call.arguments_dict.items()
                    ]
                    code = f"{function_call.name}({', '.join(arguments_materialised)})"

                    await send_code_delta_for_code(code)
                else:
                    # We have a string in the arguments, thats probably the code
                    await send_code_delta_for_code(function_call.arguments)
