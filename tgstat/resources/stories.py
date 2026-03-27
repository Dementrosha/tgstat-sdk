from __future__ import annotations

from collections.abc import Sequence

from ..models.common import Story
from ..models.stories.stat import StoryStatistics
from ..models.stories.stat_multi import StoryStatMultiItem
from ..transport import TGStatTransport
from ..types import ChannelIdentifier, StoryIdentifier


class StoriesResource:
    def __init__(
        self,
        transport: TGStatTransport,
    ) -> None:
        self._transport = transport

    async def get(self, *, story_id: StoryIdentifier) -> Story:
        """Получить одну историю."""
        return await self._transport.request(
            "GET",
            "/stories/get",
            response_model=Story,
            params={"storyId": story_id},
        )

    async def stat(self, *, story_id: StoryIdentifier) -> StoryStatistics:
        """Получить статистику истории."""
        return await self._transport.request(
            "GET",
            "/stories/stat",
            response_model=StoryStatistics,
            params={"storyId": story_id},
        )

    async def stat_multi(
        self,
        *,
        channel_id: ChannelIdentifier,
        stories_ids: Sequence[int],
    ) -> list[StoryStatMultiItem]:
        """Получить статистику по нескольким историям канала."""
        return await self._transport.request(
            "GET",
            "/stories/stat-multi",
            response_model=list[StoryStatMultiItem],
            params={"channelId": channel_id, "storiesIds": stories_ids},
        )
