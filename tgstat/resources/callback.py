from __future__ import annotations

from ..enums import CallbackEventType, PeerType, SubscriptionType
from ..models.callback import SetCallbackURLResponse, UnsubscribeResponse
from ..models.common import CallbackInfo, SubscriptionResponse, SubscriptionsList
from ..transport import TGStatTransport
from ..types import ChannelIdentifier


class CallbackResource:
    def __init__(
        self,
        transport: TGStatTransport,
    ) -> None:
        self._transport = transport

    async def set_callback_url(
        self,
        *,
        callback_url: str,
        verify_code: str | None = None,
    ) -> SetCallbackURLResponse:
        """Установить Callback URL для уведомлений TGStat."""
        return await self._transport.request(
            "POST",
            "/callback/set-callback-url",
            response_model=SetCallbackURLResponse,
            unwrap_response=False,
            data={"callback_url": callback_url, "verify_code": verify_code},
        )

    async def get_callback_info(self) -> CallbackInfo:
        """Получить информацию о текущем Callback URL."""
        return await self._transport.request(
            "GET",
            "/callback/get-callback-info",
            response_model=CallbackInfo,
        )

    async def subscribe_channel(
        self,
        *,
        channel_id: ChannelIdentifier,
        event_types: list[CallbackEventType | str],
        subscription_id: int | None = None,
    ) -> SubscriptionResponse:
        """Подписаться на события канала или обновить существующую подписку."""
        return await self._transport.request(
            "POST",
            "/callback/subscribe-channel",
            response_model=SubscriptionResponse,
            data={
                "subscription_id": subscription_id,
                "channel_id": channel_id,
                "event_types": event_types,
            },
        )

    async def subscribe_word(
        self,
        *,
        query: str,
        event_types: list[CallbackEventType | str],
        subscription_id: int | None = None,
        strong_search: bool | None = None,
        minus_words: str | None = None,
        extended_syntax: bool | None = None,
        peer_types: PeerType | str | None = None,
    ) -> SubscriptionResponse:
        """Подписаться на уведомления по ключевому слову."""
        return await self._transport.request(
            "POST",
            "/callback/subscribe-word",
            response_model=SubscriptionResponse,
            data={
                "subscription_id": subscription_id,
                "q": query,
                "event_types": event_types,
                "strong_search": strong_search,
                "minus_words": minus_words,
                "extended_syntax": extended_syntax,
                "peer_types": peer_types,
            },
        )

    async def subscriptions_list(
        self,
        *,
        subscription_id: int | None = None,
        subscription_type: SubscriptionType | str | None = None,
    ) -> SubscriptionsList:
        """Получить список активных callback-подписок."""
        return await self._transport.request(
            "GET",
            "/callback/subscriptions-list",
            response_model=SubscriptionsList,
            params={
                "subscription_id": subscription_id,
                "subscription_type": subscription_type,
            },
        )

    async def unsubscribe(self, *, subscription_id: int) -> UnsubscribeResponse:
        """Отменить подписку по её идентификатору."""
        return await self._transport.request(
            "POST",
            "/callback/unsubscribe",
            response_model=UnsubscribeResponse,
            unwrap_response=False,
            data={"subscription_id": subscription_id},
        )
