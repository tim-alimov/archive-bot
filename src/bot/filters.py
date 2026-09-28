from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery, Message

from src.core.settings import Settings


class IsAdmin(BaseFilter):
    async def __call__(
        self, event: Message | CallbackQuery, settings: Settings
    ) -> bool:
        user = event.from_user
        if user is None:
            return False
        return user.id == settings.admin_id
