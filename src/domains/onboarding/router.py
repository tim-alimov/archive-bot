from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from src.core.filters import IsAdmin
from src.domains.category.keyboards import get_category_keyboard
from src.domains.onboarding.keyboards import get_onboarding_keyboard

router = Router()


@router.message(CommandStart(deep_link=False), IsAdmin())
async def admin_start_handler(message: Message) -> None:
    await message.answer(
        """
👋 Welcome to Archive
Save messages, files, and documents to your personal archive.
To archive something:
• Send or forward it to me
• Or reply to a message with /archive
I'll ask you to choose a category, then save it to the archive.
""",
        reply_markup=get_onboarding_keyboard(),
    )


@router.message(CommandStart(deep_link=False))
async def start_handler(message: Message) -> None:
    await message.answer("Hello!", reply_markup=get_category_keyboard())


@router.message(CommandStart(deep_link=True))
async def deep_link_handler(message: Message) -> None:
    await message.answer("Deep link!")
