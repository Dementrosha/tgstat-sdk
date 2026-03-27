from __future__ import annotations

from collections.abc import Mapping
from datetime import datetime
from typing import Any

import httpx
from pydantic import TypeAdapter, ValidationError

from .config import TGStatConfig
from .exceptions import (
    ModelValidationError,
    NetworkError,
    ResponseDecodeError,
    SSLTransportError,
    TimeoutError,
    UnexpectedResponseError,
    map_api_error,
)
from .models.envelope import ErrorEnvelope
from .retry import DEFAULT_RETRYABLE_STATUS_CODES, sleep_before_retry


class TGStatTransport:
    def __init__(
        self,
        config: TGStatConfig,
        *,
        client: httpx.AsyncClient | None = None,
    ) -> None:
        self._config = config
        self._owns_client = client is None
        self._client = client or httpx.AsyncClient(
            base_url=config.base_url.rstrip("/"),
            timeout=config.timeout,
            headers={"User-Agent": config.user_agent},
        )

    async def aclose(self) -> None:
        if self._owns_client:
            await self._client.aclose()

    async def request(
        self,
        method: str,
        path: str,
        *,
        response_model: Any,
        unwrap_response: bool = True,
        params: Mapping[str, Any] | None = None,
        data: Mapping[str, Any] | None = None,
        json_data: Mapping[str, Any] | None = None,
    ) -> Any:
        prepared_params = self._prepare_mapping(params)
        prepared_data = self._prepare_mapping(data)
        prepared_json = self._prepare_mapping(json_data)
        prepared_params.setdefault("token", self._config.token)
        if method.upper() == "POST" and prepared_data is not None:
            prepared_data.setdefault("token", self._config.token)
        if method.upper() == "POST" and prepared_json is not None:
            prepared_json.setdefault("token", self._config.token)

        last_error: Exception | None = None
        validator = TypeAdapter(response_model)

        for attempt in range(1, self._config.retry.max_attempts + 1):
            try:
                response = await self._client.request(
                    method=method.upper(),
                    url=path,
                    params=prepared_params or None,
                    data=prepared_data or None,
                    json=prepared_json or None,
                )
                if response.status_code in DEFAULT_RETRYABLE_STATUS_CODES and attempt < self._config.retry.max_attempts:
                    await sleep_before_retry(attempt, self._config.retry)
                    continue

                payload = response.json()
                if not isinstance(payload, dict):
                    raise UnexpectedResponseError("Expected a top-level JSON object from TGStat API.")

                if payload.get("status") == "error":
                    try:
                        error_envelope = ErrorEnvelope.model_validate(payload)
                    except ValidationError as exc:
                        raise ModelValidationError("Failed to validate TGStat error envelope.") from exc
                    raise map_api_error(error_envelope.model_dump())

                model_payload = payload.get("response") if unwrap_response else payload
                if unwrap_response and "response" not in payload:
                    raise UnexpectedResponseError("Expected a 'response' object in TGStat API payload.")

                try:
                    return validator.validate_python(model_payload)
                except ValidationError as exc:
                    raise ModelValidationError(
                        f"Failed to validate response for {method.upper()} {path}."
                    ) from exc
            except httpx.TimeoutException as exc:
                last_error = TimeoutError(str(exc))
            except httpx.ConnectError as exc:
                last_error = NetworkError(str(exc))
            except httpx.NetworkError as exc:
                last_error = NetworkError(str(exc))
            except httpx.ReadError as exc:
                last_error = NetworkError(str(exc))
            except httpx.ProtocolError as exc:
                last_error = NetworkError(str(exc))
            except httpx.HTTPError as exc:
                if "ssl" in str(exc).lower():
                    last_error = SSLTransportError(str(exc))
                else:
                    last_error = NetworkError(str(exc))
            except ValueError as exc:
                raise ResponseDecodeError("Failed to decode TGStat response as JSON.") from exc

            if attempt >= self._config.retry.max_attempts or not isinstance(last_error, (TimeoutError, NetworkError, SSLTransportError)):
                break
            await sleep_before_retry(attempt, self._config.retry)

        if last_error is None:
            raise UnexpectedResponseError("TGStat request failed without a captured exception.")
        raise last_error

    @staticmethod
    def _prepare_mapping(mapping: Mapping[str, Any] | None) -> dict[str, Any]:
        if mapping is None:
            return {}

        prepared: dict[str, Any] = {}
        for key, value in mapping.items():
            if value is None:
                continue
            if isinstance(value, datetime):
                prepared[key] = int(value.timestamp())
            elif isinstance(value, bool):
                prepared[key] = int(value)
            elif isinstance(value, (list, tuple, set)):
                prepared[key] = ",".join(str(item) for item in value)
            else:
                prepared[key] = value
        return prepared
