from __future__ import annotations

from typing import Any

from pydantic import Field

from .base import TGStatModel


class RKNVerification(TGStatModel):
    status: str | None = None
    link:   str | None = None


class TGStatRestrictions(TGStatModel):
    red_label:   bool | None = None
    black_label: bool | None = None


class Channel(TGStatModel):
    id:                  int
    tg_id:               int | None = None
    link:                str
    peer_type:           str | None = None
    username:            str | None = None
    active_usernames:    list[str] | None = None
    title:               str
    about:               str | None = None
    category:            str | None = None
    country:             str | None = None
    language:            str | None = None
    image100:            str | None = None
    image640:            str | None = None
    participants_count:  int | None = None
    ci_index:            float | None = None
    rkn_verification:    RKNVerification | None = None
    tgstat_restrictions: TGStatRestrictions | list[Any] | None = None
    created_at:          int | None = None


class User(TGStatModel):
    id:        int
    tg_id:     int | None = None
    username:  str | None = None
    firstname: str | None = None
    lastname:  str | None = None


class Media(TGStatModel):
    media_type:         str | None = None
    caption:            str | None = None
    size:               int | None = None
    file_size:          int | None = None
    file_url:           str | None = None
    file_thumbnail_url: str | None = None
    file_name:          str | None = None
    mime_type:          str | None = None
    url:                str | None = None
    type:               str | None = None
    site_name:          str | None = None
    title:              str | None = None
    description:        str | None = None
    author:             str | None = None


class Post(TGStatModel):
    id:              int
    date:            int
    views:           int | None = None
    shares_count:    int | None = None
    comments_count:  int | None = None
    reactions_count: int | None = None
    link:            str
    channel_id:      int
    forwarded_from:  int | None = None
    user_id:         int | None = None
    is_deleted:      int | None = None
    deleted_at:      int | None = None
    group_id:        int | None = None
    text:            str | None = None
    snippet:         str | None = None
    media:           Media | None = None


class Story(TGStatModel):
    id:         int
    date:       int
    views:      int | None = None
    link:       str
    channel_id: int
    is_expired: int | None = None
    expire_at:  int | None = None
    caption:    str | None = None
    media:      Media | None = None


class ViewsGrowth(TGStatModel):
    date:         str
    views_growth: int = Field(alias="viewsGrowth")


class CallbackInfo(TGStatModel):
    url:                  str
    pending_update_count: int
    last_error_date:      int | None = None
    last_error_message:   str | None = None


class SubscriptionResponse(TGStatModel):
    subscription_id: int


class CallbackSubscription(TGStatModel):
    subscription_id:   int
    event_types:       list[str]
    subscription_type: str
    channel_id:        int | None = None
    q:                 str | None = None
    peer_types:        str | None = None
    strong_search:     int | None = None
    minus_words:       str | None = None
    extended_syntax:   int | None = None


class SubscriptionsList(TGStatModel):
    total_count:   int
    subscriptions: list[CallbackSubscription]


class CallbackEvent(TGStatModel):
    subscription_id:   int
    subscription_type: str
    event_id:          int
    event_type:        str
    post:              Post
    channels:          list[Channel]
    users:             list[User] | None = None


class DatabaseItem(TGStatModel):
    code: str | int
    name: str


class UsageStatItem(TGStatModel):
    service_key:    str | None = Field(default=None, alias="serviceKey")
    title:          str | None = None
    spent_channels: str | None = Field(default=None, alias="spentChannels")
    spent_requests: str | None = Field(default=None, alias="spentRequests")
    expired_at:     int | None = Field(default=None, alias="expiredAt")
    spent_words:    str | None = Field(default=None, alias="spentWords")
    spent_objects:  str | None = Field(default=None, alias="spentObjects")
