import asyncio

from tgstat import TGStatClient

TOKEN = "paste-your-token-here"


async def main() -> None:
    async with TGStatClient(token=TOKEN) as client:
        # response — это объект канала или чата со всеми основными полями.
        response = await client.channels.get(channel_id="@durov")
        channel = response

        print("ID:",          channel.id)
        print("Username:",    channel.username)
        print("Название:",    channel.title)
        print("Подписчики:",  channel.participants_count)
        print("Язык:",        channel.language)


if __name__ == "__main__":
    asyncio.run(main())
