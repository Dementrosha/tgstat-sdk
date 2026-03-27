import asyncio

from tgstat import TGStatClient

TOKEN = "paste-your-token-here"


async def main() -> None:
    async with TGStatClient(token=TOKEN) as client:
        # Сначала получаем реальный пост из канала, затем запрашиваем его отдельно.
        channel_posts = await client.channels.posts(channel_id="@durov", limit=1)
        if not channel_posts.items:
            print("У канала не нашлось доступных публикаций для примера.")
            return
        source_post = channel_posts.items[0]

        response = await client.posts.get(post_id=source_post.id)
        post = response

        print("ID:",        post.id)
        print("Ссылка:",    post.link)
        print("Дата:",      post.date)
        print("Просмотры:", post.views)
        print("Текст:",     post.text)


if __name__ == "__main__":
    asyncio.run(main())

