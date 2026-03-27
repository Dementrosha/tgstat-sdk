from __future__ import annotations

from datetime import datetime
from typing import TypeAlias

ChannelIdentifier: TypeAlias = int | str
PostIdentifier:    TypeAlias = int | str
StoryIdentifier:   TypeAlias = int | str
TimestampLike:     TypeAlias = int | float | datetime
