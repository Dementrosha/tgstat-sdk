import asyncio

from tgstat import TGStatClient

TOKEN = "paste-your-token-here"


async def main() -> None:
    async with TGStatClient(token=TOKEN) as client:
        # response.items — истории канала.
        response = await client.channels.stories(channel_id="@durov", limit=5)

        for story in response.items:
            print("Story ID:",  story.id)
            print("Дата:",      story.date)
            print("Просмотры:", story.views)
            print("Ссылка:",    story.link)
            print("Подпись:",   story.caption)
            print("-" * 40)


if __name__ == "__main__":
    asyncio.run(main())
