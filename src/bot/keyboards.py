from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from src.bot import texts


def get_admin_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=texts.BTN_ADD_CATEGORY)],
            [KeyboardButton(text="Category 2")],
            [KeyboardButton(text="Category 3")],
        ],
        resize_keyboard=True,
    )


def get_user_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Category 1")],
            [KeyboardButton(text="Category 2")],
            [KeyboardButton(text="Category 3")],
        ],
        resize_keyboard=True,
    )
