import asyncio

from tgstat import TGStatClient

TOKEN = "paste-your-token-here"


async def main() -> None:
    async with TGStatClient(token=TOKEN) as client:
        # Если TGStat требует подтверждение URL, сначала получите verify_code
        # из ответа API и затем повторите вызов с этим кодом.
        response = await client.callback.set_callback_url(
            callback_url="https://example.com/tgstat-callback",
        )
        print("Статус:", response.status)


if __name__ == "__main__":
    asyncio.run(main())
