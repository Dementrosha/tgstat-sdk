import asyncio

from tgstat import TGStatClient

TOKEN = "paste-your-token-here"


async def main() -> None:
    async with TGStatClient(token=TOKEN) as client:
        # response — агрегированная статистика канала или чата.
        response = await client.channels.stat(channel_id="@durov")
        stat = response

        print("ID:",                      stat.id)
        print("Название:",               stat.title)
        print("Username:",               stat.username)
        print("Тип:",                    stat.peer_type)
        print("Подписчики:",             stat.participants_count)
        print("Средний охват:",          stat.avg_post_reach)
        print("Рекламный охват 12ч:",    stat.adv_post_reach_12h)
        print("Рекламный охват 24ч:",    stat.adv_post_reach_24h)
        print("Рекламный охват 48ч:",    stat.adv_post_reach_48h)
        print("ERR%:",                   stat.err_percent)
        print("ERR24%:",                 stat.err24_percent)
        print("ER%:",                    stat.er_percent)
        print("Дневной охват:",          stat.daily_reach)
        print("CI index:",               stat.ci_index)
        print("Упоминания:",             stat.mentions_count)
        print("Репосты:",                stat.forwards_count)
        print("Кол-во упоминающих:",     stat.mentioning_channels_count)
        print("Кол-во постов:",          stat.posts_count)


if __name__ == "__main__":
    asyncio.run(main())
