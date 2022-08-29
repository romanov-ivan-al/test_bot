from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import client_kb
from aiogram.types import ReplyKeyboardRemove

async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, "Эй ты че жрешь?", reply_markup=client_kb.kb_client)
        await message.delete()
    except:
        await message.reply("Общение с ботом через ЛС, напишите ему.")


async def open_work(message: types.Message):
    await message.answer("клавиатура удалена!", reply_markup=ReplyKeyboardRemove())


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=["start", "help"])
    dp.register_message_handler(open_work, commands=['Удалить клавиатуру'])
