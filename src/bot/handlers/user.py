from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from src.bot import texts
from src.bot.keyboards import get_user_keyboard

router = Router(name=__name__)


@router.message(CommandStart(deep_link=False))
async def start_handler(message: Message) -> None:
    await message.answer(texts.USER_WELCOME, reply_markup=get_user_keyboard())


@router.message(CommandStart(deep_link=True))
async def deep_link_handler(message: Message) -> None:
    await message.answer(texts.DEEP_LINK_RECEIVED)
