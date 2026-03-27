from __future__ import annotations

from pydantic import Field

from ..base import TGStatModel


class PostStatMultiItem(TGStatModel):
    post_id:         int = Field(alias="postId")
    views_count:     int = Field(alias="viewsCount")
    shares_count:    int | None = Field(default=None, alias="sharesCount")
    comments_count:  int | None = Field(default=None, alias="commentsCount")
    reactions_count: int | None = Field(default=None, alias="reactionsCount")
