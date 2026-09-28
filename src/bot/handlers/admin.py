from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.bot import texts
from src.bot.filters import IsAdmin
from src.bot.keyboards import get_admin_keyboard
from src.bot.states import CategoryForm
from src.domain.exceptions import CategoryAlreadyExistsError, InvalidCategoryError
from src.domain.service import CategoryService

router = Router(name=__name__)
router.message.filter(IsAdmin())
router.callback_query.filter(IsAdmin())


@router.message(CommandStart(deep_link=False))
async def admin_start_handler(message: Message) -> None:
    await message.answer(texts.ADMIN_WELCOME, reply_markup=get_admin_keyboard())


@router.message(F.text == texts.BTN_ADD_CATEGORY)
async def add_category(message: Message, state: FSMContext) -> None:
    await message.answer(texts.ASK_CATEGORY_TITLE)
    await state.set_state(CategoryForm.waiting_for_title)


@router.message(CategoryForm.waiting_for_title, F.text)
async def waiting_for_title(message: Message, state: FSMContext) -> None:
    await state.update_data(title=message.text)
    await message.answer(texts.ASK_CATEGORY_DESCRIPTION)
    await state.set_state(CategoryForm.waiting_for_description)


@router.message(CategoryForm.waiting_for_description, F.text)
async def waiting_for_description(
    message: Message, state: FSMContext, category_service: CategoryService
) -> None:
    data = await state.get_data()
    await state.clear()

    try:
        await category_service.create(title=data["title"], description=message.text)
    except CategoryAlreadyExistsError:
        await message.answer(texts.CATEGORY_ALREADY_EXISTS)
        return
    except InvalidCategoryError as error:
        await message.answer(str(error))
        return

    await message.answer(texts.CATEGORY_CREATED)
