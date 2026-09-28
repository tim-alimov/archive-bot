from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from src.core.database import session_factory
from src.core.logging import setup_logging
from src.core.middlewares.dependencies import DependencyMiddleware
from src.core.settings import settings
from src.domains.onboarding.router import router as onboarding_router


async def main():
    setup_logging()
    bot = Bot(
        token=settings.bot_token.get_secret_value(),
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher()
    dp.update.middleware(DependencyMiddleware(session_factory=session_factory))

    dp.include_router(onboarding_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
