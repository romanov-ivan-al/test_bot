from aiogram import types
from create_bot import dp
import json, string


@dp.message_handler()
async def message_hendler(message: types.Message):
    if {i.lower().translate(str.maketrans("", "", string.punctuation)) for i in message.text.split(" ")}\
        .intersection(set(json.load(open("../materials/cenz.json")))) != set():
        await message.reply("Дружище, мы тут не ругаемся!")
        await message.delete()
