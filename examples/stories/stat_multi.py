import asyncio

from tgstat import TGStatClient

TOKEN = "paste-your-token-here"


async def main() -> None:
    async with TGStatClient(token=TOKEN) as client:
        channel_stories = await client.channels.stories(channel_id="@durov", limit=3)
        story_ids = [story.id for story in channel_stories.items]

        if not story_ids:
            print("У канала не нашлось доступных историй для примера.")
            return

        response = await client.stories.stat_multi(channel_id="@durov", stories_ids=story_ids)

        for item in response:
            print("Story ID:",   item.story_id)
            print("Просмотры:",  item.views_count)
            print("Репосты:",    item.forwards_count)
            print("Реакции:",    item.reactions_count)
            print("-" * 40)


if __name__ == "__main__":
    asyncio.run(main())

