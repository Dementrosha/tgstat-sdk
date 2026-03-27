import asyncio

from tgstat import TGStatClient

TOKEN = "paste-your-token-here"


async def main() -> None:
    async with TGStatClient(token=TOKEN) as client:
        # items — текущая страница найденных постов, total_count — всего результатов.
        response = await client.posts.search(query="bitcoin", limit=5, hide_forwards=True)

        print("На этой странице:", response.count)
        print("Всего найдено:",    response.total_count)

        for post in response.items:
            print(post.id, post.link, (post.text or "")[:120])


if __name__ == "__main__":
    asyncio.run(main())

