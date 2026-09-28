from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def get_onboarding_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Add a category")],
            [KeyboardButton(text="Category 2")],
            [KeyboardButton(text="Category 3")],
        ],
        resize_keyboard=True,
    )
    return keyboard
