from email.message import Message
from pydoc import text
import string
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import json, string

bot = Bot(token="5796960009:AAEHQj0Y5DuqOYJ0o_mv4gsi5NbJ4pdyWu8")
dp = Dispatcher(bot)

async def on_startup(_):
    print("Bot starts")

##########################клиентская часть###############################

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




@dp.message_handler()
async def message_hendler(message: types.Message):
    if {i.lower().translate(str.maketrans("", "", string.punctuation)) for i in message.text.split(" ")}\
        .intersection(set(json.load(open("../materials/cenz.json")))) != set():
        await message.reply("Дружище, мы тут не ругаемся!")
        await message.delete()

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
