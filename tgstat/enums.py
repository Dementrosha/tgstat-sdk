from __future__ import annotations

from enum import Enum


class StrEnum(str, Enum):
    def __str__(self) -> str:
        return self.value


class PeerType(StrEnum):
    CHANNEL = "channel"
    CHAT    = "chat"
    ALL     = "all"


class ChannelSearchPeerType(StrEnum):
    CHANNEL = "channel"
    CHAT    = "chat"
    ALL     = "all"


class ChannelsGroup(StrEnum):
    DAY   = "day"
    WEEK  = "week"
    MONTH = "month"


class SubscribersGroup(StrEnum):
    HOUR  = "hour"
    DAY   = "day"
    WEEK  = "week"
    MONTH = "month"


class PostsStatGroup(StrEnum):
    HOUR = "hour"
    DAY  = "day"


class SubscriptionType(StrEnum):
    CHANNEL = "channel"
    KEYWORD = "keyword"


class CallbackEventType(StrEnum):
    NEW_POST    = "new_post"
    EDIT_POST   = "edit_post"
    REMOVE_POST = "remove_post"


class MediaType(StrEnum):
    DOCUMENT = "mediaDocument"
    WEB_PAGE = "mediaWebPage"
    PHOTO    = "mediaPhoto"
    GEO      = "mediaGeo"
    CONTACT  = "mediaContact"
    VENUE    = "mediaVenue"
    GEO_LIVE = "mediaGeoLive"
    GAME     = "mediaGame"
    INVOICE  = "mediaInvoice"


class ResponseStatus(StrEnum):
    OK      = "ok"
    ERROR   = "error"
    PENDING = "pending"
