from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from src.core.settings import settings


async def main():
    bot = Bot(
        token=settings.bot_token.get_secret_value(),
        parse_mode=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher()

    await dp.start_polling(bot)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
