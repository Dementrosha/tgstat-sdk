from __future__ import annotations

from ..enums import ChannelSearchPeerType, ChannelsGroup, SubscribersGroup
from ..models.channels.add import AddChannelPendingResponse
from ..models.channels.avg_posts_reach import AvgPostsReachPeriod
from ..models.channels.er import ERPeriod
from ..models.channels.err import ERRPeriod
from ..models.channels.err24 import ERR24Period
from ..models.channels.forwards import ChannelForwardsResult
from ..models.channels.mentions import ChannelMentionsResult
from ..models.channels.posts import ChannelPostsResult
from ..models.channels.search import ChannelSearchPayload
from ..models.channels.stat import ChannelStatPayload
from ..models.channels.stories import ChannelStoriesResult
from ..models.channels.subscribers import SubscribersPeriod
from ..models.channels.views import ViewsPeriod
from ..models.common import Channel
from ..transport import TGStatTransport
from ..types import ChannelIdentifier, TimestampLike


class ChannelsResource:
    def __init__(
        self,
        transport: TGStatTransport,
    ) -> None:
        self._transport = transport

    async def get(self, *, channel_id: ChannelIdentifier) -> Channel:
        """Получить карточку канала или чата."""
        return await self._transport.request(
            "GET",
            "/channels/get",
            response_model=Channel,
            params={"channelId": channel_id},
        )

    async def search(
        self,
        *,
        query: str | None = None,
        search_by_description: bool | None = None,
        peer_type: ChannelSearchPeerType | str | None = None,
        country: str | None = None,
        language: str | None = None,
        category: str | None = None,
        limit: int | None = None,
    ) -> ChannelSearchPayload:
        """Найти каналы или чаты по запросу и фильтрам."""
        return await self._transport.request(
            "GET",
            "/channels/search",
            response_model=ChannelSearchPayload,
            params={
                "q": query,
                "search_by_description": search_by_description,
                "peer_type": peer_type,
                "country": country,
                "language": language,
                "category": category,
                "limit": limit,
            },
        )

    async def stat(self, *, channel_id: ChannelIdentifier) -> ChannelStatPayload:
        """Получить сводную статистику канала."""
        return await self._transport.request(
            "GET",
            "/channels/stat",
            response_model=ChannelStatPayload,
            params={"channelId": channel_id},
        )

    async def posts(
        self,
        *,
        channel_id: ChannelIdentifier,
        limit: int | None = None,
        offset: int | None = None,
        start_time: TimestampLike | None = None,
        end_time: TimestampLike | None = None,
        hide_forwards: bool | None = None,
        hide_deleted: bool | None = None,
        extended: bool | None = None,
    ) -> ChannelPostsResult:
        """Получить список публикаций канала."""
        return await self._transport.request(
            "GET",
            "/channels/posts",
            response_model=ChannelPostsResult,
            params={
                "channelId": channel_id,
                "limit": limit,
                "offset": offset,
                "startTime": start_time,
                "endTime": end_time,
                "hideForwards": hide_forwards,
                "hideDeleted": hide_deleted,
                "extended": extended,
            },
        )

    async def stories(
        self,
        *,
        channel_id: ChannelIdentifier,
        limit: int | None = None,
        offset: int | None = None,
        start_time: TimestampLike | None = None,
        end_time: TimestampLike | None = None,
        hide_expired: bool | None = None,
        extended: bool | None = None,
    ) -> ChannelStoriesResult:
        """Получить список историй канала."""
        return await self._transport.request(
            "GET",
            "/channels/stories",
            response_model=ChannelStoriesResult,
            params={
                "channelId": channel_id,
                "limit": limit,
                "offset": offset,
                "startTime": start_time,
                "endTime": end_time,
                "hideExpired": hide_expired,
                "extended": extended,
            },
        )

    async def mentions(
        self,
        *,
        channel_id: ChannelIdentifier,
        start_date: TimestampLike | None = None,
        end_date: TimestampLike | None = None,
        limit: int | None = None,
        offset: int | None = None,
        extended: bool | None = None,
    ) -> ChannelMentionsResult:
        """Получить упоминания канала или чата."""
        return await self._transport.request(
            "GET",
            "/channels/mentions",
            response_model=ChannelMentionsResult,
            params={
                "channelId": channel_id,
                "startDate": start_date,
                "endDate": end_date,
                "limit": limit,
                "offset": offset,
                "extended": extended,
            },
        )

    async def forwards(
        self,
        *,
        channel_id: ChannelIdentifier,
        start_date: TimestampLike | None = None,
        end_date: TimestampLike | None = None,
        limit: int | None = None,
        offset: int | None = None,
        extended: bool | None = None,
    ) -> ChannelForwardsResult:
        """Получить репосты публикаций канала."""
        return await self._transport.request(
            "GET",
            "/channels/forwards",
            response_model=ChannelForwardsResult,
            params={
                "channelId": channel_id,
                "startDate": start_date,
                "endDate": end_date,
                "limit": limit,
                "offset": offset,
                "extended": extended,
            },
        )

    async def subscribers(
        self,
        *,
        channel_id: ChannelIdentifier,
        start_date: TimestampLike | None = None,
        end_date: TimestampLike | None = None,
        group: SubscribersGroup | str | None = None,
    ) -> list[SubscribersPeriod]:
        """Получить динамику подписчиков."""
        return await self._transport.request(
            "GET",
            "/channels/subscribers",
            response_model=list[SubscribersPeriod],
            params={
                "channelId": channel_id,
                "startDate": start_date,
                "endDate": end_date,
                "group": group,
            },
        )

    async def views(
        self,
        *,
        channel_id: ChannelIdentifier,
        start_date: TimestampLike | None = None,
        end_date: TimestampLike | None = None,
        group: ChannelsGroup | str | None = None,
    ) -> list[ViewsPeriod]:
        """Получить динамику суммарных просмотров канала."""
        return await self._transport.request(
            "GET",
            "/channels/views",
            response_model=list[ViewsPeriod],
            params={
                "channelId": channel_id,
                "startDate": start_date,
                "endDate": end_date,
                "group": group,
            },
        )

    async def avg_posts_reach(
        self,
        *,
        channel_id: ChannelIdentifier,
        start_date: TimestampLike | None = None,
        end_date: TimestampLike | None = None,
        group: ChannelsGroup | str | None = None,
    ) -> list[AvgPostsReachPeriod]:
        """Получить динамику среднего охвата публикаций."""
        return await self._transport.request(
            "GET",
            "/channels/avg-posts-reach",
            response_model=list[AvgPostsReachPeriod],
            params={
                "channelId": channel_id,
                "startDate": start_date,
                "endDate": end_date,
                "group": group,
            },
        )

    async def er(
        self,
        *,
        channel_id: ChannelIdentifier,
        start_date: TimestampLike | None = None,
        end_date: TimestampLike | None = None,
        group: ChannelsGroup | str | None = None,
    ) -> list[ERPeriod]:
        """Получить динамику показателя ER."""
        return await self._transport.request(
            "GET",
            "/channels/er",
            response_model=list[ERPeriod],
            params={
                "channelId": channel_id,
                "startDate": start_date,
                "endDate": end_date,
                "group": group,
            },
        )

    async def err(
        self,
        *,
        channel_id: ChannelIdentifier,
        start_date: TimestampLike | None = None,
        end_date: TimestampLike | None = None,
        group: ChannelsGroup | str | None = None,
    ) -> list[ERRPeriod]:
        """Получить динамику показателя ERR."""
        return await self._transport.request(
            "GET",
            "/channels/err",
            response_model=list[ERRPeriod],
            params={
                "channelId": channel_id,
                "startDate": start_date,
                "endDate": end_date,
                "group": group,
            },
        )

    async def err24(
        self,
        *,
        channel_id: ChannelIdentifier,
        start_date: TimestampLike | None = None,
        end_date: TimestampLike | None = None,
        group: ChannelsGroup | str | None = None,
    ) -> list[ERR24Period]:
        """Получить динамику показателя ERR24."""
        return await self._transport.request(
            "GET",
            "/channels/err24",
            response_model=list[ERR24Period],
            params={
                "channelId": channel_id,
                "startDate": start_date,
                "endDate": end_date,
                "group": group,
            },
        )

    async def add(
        self,
        *,
        channel_name: str,
        country: str | None = None,
        language: str | None = None,
        category: str | None = None,
    ) -> AddChannelPendingResponse:
        """Поставить канал в очередь на добавление в базу TGStat."""
        return await self._transport.request(
            "POST",
            "/channels/add",
            response_model=AddChannelPendingResponse,
            unwrap_response=False,
            json_data={
                "channelName": channel_name,
                "country": country,
                "language": language,
                "category": category,
            },
        )
