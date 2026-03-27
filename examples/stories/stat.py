import asyncio

from tgstat import TGStatClient

TOKEN = "paste-your-token-here"


async def main() -> None:
    async with TGStatClient(token=TOKEN) as client:
        # Берём реальную историю канала и по её ID запрашиваем статистику.
        channel_stories = await client.channels.stories(channel_id="@durov", limit=1)
        if not channel_stories.items:
            print("У канала не нашлось доступных историй для примера.")
            return
        source_story = channel_stories.items[0]

        response = await client.stories.stat(story_id=source_story.id)
        stat = response

        print("Просмотры:", stat.views_count)
        print("Репосты:",   stat.forwards_count)
        print("Реакции:",   stat.reactions_count)

        if stat.views:
            for item in stat.views[:3]:
                print(item.date, item.views_growth)


if __name__ == "__main__":
    asyncio.run(main())

