from __future__ import annotations

from pydantic import Field

from ..base import TGStatModel


class StoryStatMultiItem(TGStatModel):
    story_id:        int = Field(alias="storyId")
    views_count:     int = Field(alias="viewsCount")
    forwards_count:  int | None = Field(default=None, alias="forwardsCount")
    reactions_count: int | None = Field(default=None, alias="reactionsCount")
