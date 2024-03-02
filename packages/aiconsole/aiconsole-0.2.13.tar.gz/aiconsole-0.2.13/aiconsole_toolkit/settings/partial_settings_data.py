from typing import Any, Optional

from pydantic import BaseModel

from aiconsole.core.gpt.types import GPTModeConfig
from aiconsole.core.users.types import PartialUserProfile


class PartialSettingsData(BaseModel):
    code_autorun: Optional[bool] = None
    openai_api_key: Optional[str] = None
    user_profile: Optional[PartialUserProfile] = None
    assets: Optional[dict[str, bool]] = None
    assets_to_reset: Optional[list[str]] = None
    gpt_modes: Optional[dict[str, GPTModeConfig]] = None
    extra: Optional[dict[str, Any]] = None
