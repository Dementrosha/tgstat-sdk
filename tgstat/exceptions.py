from __future__ import annotations

from collections.abc import Mapping
from typing import Any


class TGStatError(Exception):
    """Base class for TGStat SDK errors."""


class TransportError(TGStatError):
    """Base class for transport-level failures."""


class NetworkError(TransportError):
    """Raised for network failures."""


class TimeoutError(TransportError):
    """Raised for request timeouts."""


class SSLTransportError(TransportError):
    """Raised for TLS or SSL transport errors."""


class ResponseDecodeError(TransportError):
    """Raised when the response payload cannot be decoded."""


class UnexpectedResponseError(TransportError):
    """Raised when TGStat returns an unexpected response payload."""


class ModelValidationError(TransportError):
    """Raised when a response cannot be validated against a Pydantic model."""


class APIError(TGStatError):
    """Base class for TGStat API-level failures."""

    def __init__(
        self,
        message: str,
        *,
        error_code: str | None = None,
        payload: Mapping[str, Any] | None = None,
    ) -> None:
        super().__init__(message)
        self.error_code = error_code
        self.payload = dict(payload or {})


class EmptyTokenError(APIError):
    """Пустой токен или токен не был передан в запросе."""


class InvalidTokenError(APIError):
    """TGStat отклонил токен как неверный или недействительный."""


class WrongMethodError(APIError):
    """Запрошен несуществующий или недоступный метод API."""


class WrongMethodTypeError(APIError):
    """Для метода использован неверный HTTP-метод запроса."""


class FloodControl10Error(APIError):
    """Сработало ограничение flood control TGStat на 10 секунд."""


class FloodControl60Error(APIError):
    """Сработало ограничение flood control TGStat на 60 секунд."""


class NoActiveSubscriptionError(APIError):
    """Для метода требуется активная подписка или тариф TGStat."""


class QuotaRequestsReachedError(APIError):
    """Исчерпана квота запросов."""


class QuotaChannelReachedError(APIError):
    """Исчерпана квота на количество отслеживаемых каналов."""


class QuotaKeywordsReachedError(APIError):
    """Исчерпана квота на количество отслеживаемых ключевых слов."""


class QuotaForeignChannelError(APIError):
    """Превышено ограничение на работу с иностранными каналами."""


class QuotaCallbackObjectsReachedError(APIError):
    """Исчерпана квота callback-объектов."""


class OutdatedStatisticsError(APIError):
    """TGStat ещё не подготовил актуальную статистику по запрошенным данным."""


class UnknownTGStatError(APIError):
    """Неизвестная ошибка TGStat API."""


ERROR_CODE_MAP: dict[str, type[APIError]] = {
    "empty_token": EmptyTokenError,
    "token_invalid": InvalidTokenError,
    "wrong_method": WrongMethodError,
    "wrong_method_type": WrongMethodTypeError,
    "flood_control_10": FloodControl10Error,
    "flood_control_60": FloodControl60Error,
    "no_active_subscription": NoActiveSubscriptionError,
    "quota_requests_reached": QuotaRequestsReachedError,
    "quota_channel_reached": QuotaChannelReachedError,
    "quota_keywords_reached": QuotaKeywordsReachedError,
    "quota_foreign_channel": QuotaForeignChannelError,
    "quota_callback_objects_reached": QuotaCallbackObjectsReachedError,
    "outdated_statistics": OutdatedStatisticsError,
    "unknown_error": UnknownTGStatError,
}


def map_api_error(payload: Mapping[str, Any]) -> APIError:
    error_code = str(payload.get("error", "unknown_error"))
    error_cls = ERROR_CODE_MAP.get(error_code, APIError)
    return error_cls(error_code, error_code=error_code, payload=payload)
