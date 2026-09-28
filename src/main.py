import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from src.bot.handlers import admin, user
from src.bot.middlewares import ServiceMiddleware
from src.core.database import create_session_factory
from src.core.logging import setup_logging
from src.core.settings import Settings


async def main() -> None:
    settings = Settings()  # pyright: ignore[reportCallIssue]
    setup_logging(settings.log_level, settings.debug)

    session_factory = create_session_factory(settings.database_url.get_secret_value())

    bot = Bot(
        token=settings.bot_token.get_secret_value(),
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher(settings=settings)
    dp.update.middleware(ServiceMiddleware(session_factory=session_factory))

    # Admin router goes first so an admin's /start isn't caught by the user one.
    dp.include_routers(admin.router, user.router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
