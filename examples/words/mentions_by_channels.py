import asyncio

from tgstat import TGStatClient

TOKEN = "paste-your-token-here"


async def main() -> None:
    async with TGStatClient(token=TOKEN) as client:
        # items — агрегаты по каналам, channels — полные объекты каналов.
        response = await client.words.mentions_by_channels(query="OpenAI")

        channels_by_id = {channel.id: channel for channel in response.channels}
        for item in response.items[:5]:
            channel = channels_by_id.get(item.channel_id)
            title = channel.title if channel else "Unknown"
            print(title, item.mentions_count, item.views_count, item.last_mention_date)


if __name__ == "__main__":
    asyncio.run(main())

