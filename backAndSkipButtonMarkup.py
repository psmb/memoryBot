
from telebot import types

backAndSkipButtonMarkup = types.ReplyKeyboardMarkup(row_width=2)
backAndSkipButtonMarkup.add(types.KeyboardButton(
    'Назад'), types.KeyboardButton('Пропустить'))
