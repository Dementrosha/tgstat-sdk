from __future__ import annotations

from collections.abc import Sequence

from ..enums import PeerType, PostsStatGroup
from ..models.common import Post
from ..models.posts.search import PostSearchPayload
from ..models.posts.stat import PostStatistics
from ..models.posts.stat_multi import PostStatMultiItem
from ..transport import TGStatTransport
from ..types import ChannelIdentifier, PostIdentifier, TimestampLike


class PostsResource:
    def __init__(
        self,
        transport: TGStatTransport,
    ) -> None:
        self._transport = transport

    async def get(self, *, post_id: PostIdentifier) -> Post:
        """Получить одну публикацию по идентификатору."""
        return await self._transport.request(
            "GET",
            "/posts/get",
            response_model=Post,
            params={"postId": post_id},
        )

    async def stat(
        self,
        *,
        post_id: PostIdentifier,
        group: PostsStatGroup | str | None = None,
    ) -> PostStatistics:
        """Получить статистику одной публикации."""
        return await self._transport.request(
            "GET",
            "/posts/stat",
            response_model=PostStatistics,
            params={"postId": post_id, "group": group},
        )

    async def stat_multi(
        self,
        *,
        channel_id: ChannelIdentifier,
        posts_ids: Sequence[int],
    ) -> list[PostStatMultiItem]:
        """Получить статистику сразу по нескольким постам канала."""
        return await self._transport.request(
            "GET",
            "/posts/stat-multi",
            response_model=list[PostStatMultiItem],
            params={"channelId": channel_id, "postsIds": posts_ids},
        )

    async def search(
        self,
        *,
        query: str,
        limit: int | None = None,
        offset: int | None = None,
        peer_type: PeerType | str | None = None,
        start_date: TimestampLike | None = None,
        end_date: TimestampLike | None = None,
        country: str | None = None,
        language: str | None = None,
        category: str | None = None,
        hide_forwards: bool | None = None,
        hide_deleted: bool | None = None,
        strong_search: bool | None = None,
        minus_words: str | None = None,
        extended: bool | None = None,
        extended_syntax: bool | None = None,
    ) -> PostSearchPayload:
        """Найти публикации по текстовому запросу."""
        return await self._transport.request(
            "GET",
            "/posts/search",
            response_model=PostSearchPayload,
            params={
                "q": query,
                "limit": limit,
                "offset": offset,
                "peerType": peer_type,
                "startDate": start_date,
                "endDate": end_date,
                "country": country,
                "language": language,
                "category": category,
                "hideForwards": hide_forwards,
                "hideDeleted": hide_deleted,
                "strongSearch": strong_search,
                "minusWords": minus_words,
                "extended": extended,
                "extendedSyntax": extended_syntax,
            },
        )
