from __future__ import annotations

from typing import Generic, TypeVar

from pydantic import Field

from .base import TGStatModel

ResponseT = TypeVar("ResponseT")


class OkEnvelope(TGStatModel, Generic[ResponseT]):
    status:   str = Field(default="ok")
    response: ResponseT


class ErrorEnvelope(TGStatModel):
    status: str = Field(default="error")
    error:  str


class PendingEnvelope(TGStatModel):
    status: str = Field(default="pending")
