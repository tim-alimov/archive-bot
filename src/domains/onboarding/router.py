from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from src.core.filters import IsAdmin

router = Router()

@router.message(CommandStart(), IsAdmin())
async def admin_start_handler(message: Message) -> None:
    await message.answer("Hello, admin!")

@router.message(CommandStart(deep_link=False))
async def start_handler(message: Message) -> None:
    await message.answer("Hello!")
