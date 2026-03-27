import asyncio

from tgstat import TGStatClient

TOKEN = "paste-your-token-here"


async def main() -> None:
    async with TGStatClient(token=TOKEN) as client:
        # response.subscriptions — активные callback-подписки.
        response = await client.callback.subscriptions_list()

        print("Всего подписок:", response.total_count)
        for item in response.subscriptions:
            print("ID:",      item.subscription_id)
            print("Тип:",     item.subscription_type)
            print("События:", item.event_types)
            print("-" * 40)


if __name__ == "__main__":
    asyncio.run(main())

