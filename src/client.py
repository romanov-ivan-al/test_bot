from aiogram import types
from create_bot import dp, bot


@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, "Эй ты че жрешь?")
        await message.delete()
    except:
        await message.reply("Общение с ботом через ЛС, напишите ему.")


@dp.message_handler(commands=['Режим_работы'])
async def open_work(message: types.Message):
    await message.answer("когда надо тогда и работаем!")
