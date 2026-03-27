from __future__ import annotations

from ..base import TGStatModel


class ChannelStatPayload(TGStatModel):
    id:                        int
    title:                     str
    username:                  str | None = None
    peer_type:                 str
    participants_count:        int
    avg_post_reach:            int | None = None
    adv_post_reach_12h:        int | None = None
    adv_post_reach_24h:        int | None = None
    adv_post_reach_48h:        int | None = None
    err_percent:               float | None = None
    err24_percent:             float | None = None
    er_percent:                float | None = None
    daily_reach:               int | None = None
    ci_index:                  float | None = None
    mentions_count:            int | None = None
    forwards_count:            int | None = None
    mentioning_channels_count: int | None = None
    posts_count:               int | None = None
    dau:                       int | None = None
    wau:                       int | None = None
    mau:                       int | None = None
    online_count_day_time:     int | None = None
    online_count_night_time:   int | None = None
    messages_count_yesterday:  int | None = None
    messages_count_last_week:  int | None = None
    messages_count_last_month: int | None = None
    messages_count_total:      int | None = None
