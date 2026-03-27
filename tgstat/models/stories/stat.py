from __future__ import annotations

from pydantic import Field

from ..base import TGStatModel
from ..common import ViewsGrowth


class StoryStatistics(TGStatModel):
    views_count:     int = Field(alias="viewsCount")
    forwards_count:  int | None = Field(default=None, alias="forwardsCount")
    reactions_count: int | None = Field(default=None, alias="reactionsCount")
    views:           list[ViewsGrowth] | None = None
