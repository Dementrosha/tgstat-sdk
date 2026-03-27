from __future__ import annotations

from ..enums import PeerType
from ..models.words.mentions import WordMentionsPayload
from ..models.words.mentions_by_channels import WordMentionsByChannelsPayload
from ..models.words.mentions_by_period import WordMentionsByPeriodPayload
from ..models.words.reach import WordReachPayload
from ..transport import TGStatTransport
from ..types import TimestampLike


class WordsResource:
    def __init__(
        self,
        transport: TGStatTransport,
    ) -> None:
        self._transport = transport

    async def mentions(
        self,
        *,
        query: str,
        start_date: TimestampLike | None = None,
        end_date: TimestampLike | None = None,
        hide_forwards: bool | None = None,
        strong_search: bool | None = None,
        minus_words: str | None = None,
        group: str | None = None,
    ) -> WordMentionsPayload:
        """Получить динамику количества упоминаний слова или фразы."""
        return await self._transport.request(
            "GET",
            "/words/mentions",
            response_model=WordMentionsPayload,
            params={
                "q": query,
                "startDate": start_date,
                "endDate": end_date,
                "hideForwards": hide_forwards,
                "strongSearch": strong_search,
                "minusWords": minus_words,
                "group": group,
            },
        )

    async def reach(
        self,
        *,
        query: str,
        start_date: TimestampLike | None = None,
        end_date: TimestampLike | None = None,
        hide_forwards: bool | None = None,
        strong_search: bool | None = None,
        minus_words: str | None = None,
        group: str | None = None,
    ) -> WordReachPayload:
        """Получить динамику охвата по ключевому слову."""
        return await self._transport.request(
            "GET",
            "/words/reach",
            response_model=WordReachPayload,
            params={
                "q": query,
                "startDate": start_date,
                "endDate": end_date,
                "hideForwards": hide_forwards,
                "strongSearch": strong_search,
                "minusWords": minus_words,
                "group": group,
            },
        )

    async def mentions_by_period(
        self,
        *,
        query: str,
        peer_type: PeerType | str | None = None,
        start_date: TimestampLike | None = None,
        end_date: TimestampLike | None = None,
        hide_forwards: bool | None = None,
        strong_search: bool | None = None,
        minus_words: str | None = None,
        group: str | None = None,
        extended_syntax: bool | None = None,
    ) -> WordMentionsByPeriodPayload:
        """Получить упоминания по периодам с детализацией из TGStat Search API."""
        return await self._transport.request(
            "GET",
            "/words/mentions-by-period",
            response_model=WordMentionsByPeriodPayload,
            params={
                "q": query,
                "peerType": peer_type,
                "startDate": start_date,
                "endDate": end_date,
                "hideForwards": hide_forwards,
                "strongSearch": strong_search,
                "minusWords": minus_words,
                "group": group,
                "extendedSyntax": extended_syntax,
            },
        )

    async def mentions_by_channels(
        self,
        *,
        query: str,
        peer_type: PeerType | str | None = None,
        start_date: TimestampLike | None = None,
        end_date: TimestampLike | None = None,
        hide_forwards: bool | None = None,
        strong_search: bool | None = None,
        minus_words: str | None = None,
        extended_syntax: bool | None = None,
    ) -> WordMentionsByChannelsPayload:
        """Получить каналы, где упоминалось слово."""
        return await self._transport.request(
            "GET",
            "/words/mentions-by-channels",
            response_model=WordMentionsByChannelsPayload,
            params={
                "q": query,
                "peerType": peer_type,
                "startDate": start_date,
                "endDate": end_date,
                "hideForwards": hide_forwards,
                "strongSearch": strong_search,
                "minusWords": minus_words,
                "extendedSyntax": extended_syntax,
            },
        )
