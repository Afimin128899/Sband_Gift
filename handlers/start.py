from aiogram import types
from aiogram.filters import CommandStart

from dispatcher import dp
from services.flyer import flyer


@dp.message(CommandStart())
async def start(message: types.Message):
    ok = await flyer.check(
        user_id=message.from_user.id,
        language_code=message.from_user.language_code,
    )

    if not ok:
        await message.answer(
            "Привет! Для доступа нужно выполнить задания / подписаться."
        )
        return

    await message.answer("✅ Доступ разрешён")
