import asyncio

from tgstat import TGStatClient

TOKEN = "paste-your-token-here"


async def main() -> None:
    async with TGStatClient(token=TOKEN) as client:
        # Берём реальный пост из канала и по его ID запрашиваем статистику.
        channel_posts = await client.channels.posts(channel_id="@durov", limit=1)
        if not channel_posts.items:
            print("У канала не нашлось доступных публикаций для примера.")
            return
        source_post = channel_posts.items[0]

        response = await client.posts.stat(post_id=source_post.id)
        stat = response

        print("Просмотры:",   stat.views_count)
        print("Репосты:",     stat.shares_count)
        print("Комментарии:", stat.comments_count)
        print("Реакции:",     stat.reactions_count)

        if stat.views:
            print("Динамика просмотров:")
            for item in stat.views[:3]:
                print(item.date, item.views_growth)


if __name__ == "__main__":
    asyncio.run(main())

