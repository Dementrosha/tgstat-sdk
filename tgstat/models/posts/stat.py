from __future__ import annotations

from pydantic import Field

from ..base import TGStatModel
from ..common import Channel, Post, ViewsGrowth


class PostStatistics(TGStatModel):
    views_count:     int = Field(alias="viewsCount")
    shares_count:    int | None = Field(default=None, alias="sharesCount")
    comments_count:  int | None = Field(default=None, alias="commentsCount")
    reactions_count: int | None = Field(default=None, alias="reactionsCount")
    forwards_count:  int | None = Field(default=None, alias="forwardsCount")
    mentions_count:  int | None = Field(default=None, alias="mentionsCount")
    views:           list[ViewsGrowth] | None = None
    forwards:        list[Post] | None = None
    mentions:        list[Post] | None = None
    channels:        list[Channel] | None = None
