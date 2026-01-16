from aiogram import types
from aiogram.filters import Command

from dispatcher import dp


@dp.message(Command("check"))
async def check(message: types.Message):
    await message.answer(
        "Привет! Для доступа нужно выполнить задания / подписаться."
    )
