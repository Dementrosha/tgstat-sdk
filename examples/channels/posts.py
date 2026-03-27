import asyncio

from tgstat import TGStatClient

TOKEN = "paste-your-token-here"


async def main() -> None:
    async with TGStatClient(token=TOKEN) as client:
        # response.items — список публикаций канала.
        response = await client.channels.posts(channel_id="@durov", limit=3, extended=True)

        if response.channel:
            print("Канал:", response.channel.title)

        for post in response.items:
            print("Post ID:",    post.id)
            print("Дата:",       post.date)
            print("Просмотры:",  post.views)
            print("Ссылка:",     post.link)
            print("Текст:",      (post.text or "")[:120])
            print("-" * 40)


if __name__ == "__main__":
    asyncio.run(main())
