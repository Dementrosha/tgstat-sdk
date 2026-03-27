import asyncio

from tgstat import TGStatClient

TOKEN = "paste-your-token-here"


async def main() -> None:
    async with TGStatClient(token=TOKEN) as client:
        # Перед этим callback URL уже должен быть подтвержден в вашем кабинете/API.
        response = await client.callback.subscribe_word(
            query="OpenAI",
            event_types=["new_post"],
            strong_search=True,
        )
        print("ID подписки:", response.subscription_id)


if __name__ == "__main__":
    asyncio.run(main())

