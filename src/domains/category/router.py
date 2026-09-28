from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.domains.category.states import CategoryForm

router = Router(name=__name__)

@router.message(F.text == "Add a category")
async def add_category(message: Message, state: FSMContext) -> None:
    await message.answer("Please enter the category title:")
    await state.set_state(CategoryForm.waiting_for_title)

@router.message(CategoryForm.waiting_for_title)
async def waiting_for_title(message: Message, state: FSMContext) -> None:
    await state.update_data(title=message.text)
    await message.answer("Please enter the category description:")
    await state.set_state(CategoryForm.waiting_for_description)

@router.message(CategoryForm.waiting_for_description)
async def waiting_for_description(message: Message, state: FSMContext) -> None:
    await state.update_data(description=message.text)
    data = await state.get_data()

    await message.answer("Category added successfully!")
    await state.set_state(None)
