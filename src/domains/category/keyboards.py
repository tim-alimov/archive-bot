from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def get_category_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Category 1")],
            [KeyboardButton(text="Category 2")],
            [KeyboardButton(text="Category 3")],
        ],
        resize_keyboard=True,
    )
    return keyboard
