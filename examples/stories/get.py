import asyncio

from tgstat import TGStatClient

TOKEN = "paste-your-token-here"


async def main() -> None:
    async with TGStatClient(token=TOKEN) as client:
        # Сначала получаем реальную историю канала, затем запрашиваем её отдельно.
        channel_stories = await client.channels.stories(channel_id="@durov", limit=1)
        if not channel_stories.items:
            print("У канала не нашлось доступных историй для примера.")
            return
        source_story = channel_stories.items[0]

        response = await client.stories.get(story_id=source_story.id)
        story = response

        print("ID:",        story.id)
        print("Ссылка:",    story.link)
        print("Дата:",      story.date)
        print("Просмотры:", story.views)
        print("Подпись:",   story.caption)


if __name__ == "__main__":
    asyncio.run(main())

