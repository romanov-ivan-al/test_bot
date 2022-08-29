from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton("/start")
b2 = KeyboardButton("/Режим_работы")
b3 = KeyboardButton("Test_button")
#b4 = KeyboardButton("Поделиться номером",request_contact=True)
#b5 = KeyboardButton("Поделиться раположением", request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.add(b1).add(b2).insert(b3)