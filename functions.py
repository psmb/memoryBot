# data=['Алтайский край', 'Амурская область', 'Архангельская область', 'Астраханская область','Белгородская область','Брянская область','Владимирская область','Волгоградская область','Вологодская область',
#       'Воронежская область','Москва', 'Московская область', 'Еврейская автономная область','Забайкальский край','Ивановская область', 'Иркутская область','Кабардино-Балкарская Республика','Калининградская область',
#       'Калужская область','Камчатский край','Карачаево-Черкесская Республика','Кемеровская область — Кузбасс','Кировская область','Костромская область','Краснодарский край','Красноярский край','Курганская область',
#       'Курская область','Ленинградская область','Липецкая область','Магаданская область','Мурманская область','Ненецкий автономный округ','Нижегородская область','Новгородская область','Новосибирская область',
#       'Омская область','Оренбургская область','Орловская область','Пензенская область','Пермский край','Приморский край','Псковская область','Республика Адыгея','Адыгея','Республика Алтай','Республика Башкортостан',
#       'Республика Бурятия','Республика Дагестан','Республика Ингушетия','Республика Калмыкия','Республика Карелия','Республика Коми','Республика Крым','Республика Марий Эл','Республика Мордовия','Республика Саха',
#       'Якутия','Республика Северная Осетия','Алания','Республика Татарстан', 'Республика Тыва', 'Республика Хакасия','Ростовская область','Рязанская область','Самарская область','Санкт-Петербург','Саратовская область',
#       'Сахалинская область','Свердловская область','Севастополь','Смоленская область','Ставропольский край','Тамбовская область','Тверская область','Томская область','Тульская область','Тюменская область',
#       'Удмуртская Республика','Ульяновская область','Хабаровский край','Ханты-Мансийский автономный округ ','Югра','Челябинская область','Чеченская Республика','Чувашская Республика','Чувашия',
#       'Чукотский автономный округ','Ямало-Ненецкий автономный округ','Ярославская область']
#
# data = ['Алтайский край', 'Забайкальский край', 'Челябинская область']
#
# inputWord = 'Алтайский край'
#
# def firstStep(data, inputWord):
#     mabyRightWord = ''
#     rightWord = ''
#     for i in range(len(data)):
#         word_1 = data[i] #word_1 - С этим слово будут сравнивать
#         word_2 = inputWord #word_2 - ЭТО слово будут сравнивать
#         for j in range(len(word_1)):
#             for n in range(len(word_2)):
#                a = word_2[n]
#                b = word_1[j]
#                if word_2[n] == word_1[j]:
#                     mabyRightWord += word_1[j]
#                     break
#         if len(mabyRightWord) > len(rightWord):
#             rightWord = mabyRightWord
#         mabyRightWord = ''
#         print(rightWord, data[i])
#
#     return rightWord
#
#
# def secondStep(data,inputWord):
#     firstLat = ''
#
#     word_1 = inputWord #word_1 - С этим слово будут сравнивать
#     word_2 = data #word_2 - ЭТО слово будут сравнивать
#
#     for j in range(len(word_2)):
#         if firstLat != '':
#             break
#         for n in range(len(word_1)):
#             a = word_1[n]
#             b = word_2[j]
#             if word_2[j] == word_1[n]:
#                 firstLat = word_1[n]
#                 break
#     return firstLat
#
#
# def thirdStep(data, MabyRightWord):
#
#     NowCountRightLetters = 0
#     PreviousCountRightLetters = 0
#
#     for i in range(len(data)):
#         firstLat = secondStep(data[i], inputWord)
#
#         a = data[i]
#         try:
#             startLatWord_1Data = data[i].index(firstLat)
#             startLatWord_2Input = MabyRightWord.index(firstLat)
#         except:
#             continue
#
#         word_1 = data[i] #word_2 - ЭТО слово будут сравнивать
#         word_2 = MabyRightWord  # word_1 - С этим слово будут сравнивать
#
#         for j in range(startLatWord_1Data, len(word_1)):
#             for n in range(startLatWord_2Input, len(word_2)):
#                 с = word_1[j]
#                 b = word_2[n]
#                 if word_2[n] == word_1[j]:
#                     NowCountRightLetters +=1
#                     startLatWord_2Input += 1
#                     break
#         if NowCountRightLetters > PreviousCountRightLetters:
#             rightWord = data[i]
#             PreviousCountRightLetters = NowCountRightLetters
#             NowCountRightLetters = 0
#     print(rightWord)
#
#
# MabyRightWord = firstStep(data, inputWord)
# thirdStep(data, inputWord)

# import telebot
# import requests
#
# from telegram import (InlineKeyboardButton, InlineKeyboardMarkup)
#
# from class_library import User
# from telebot import types
# token = '5043105684:AAEHWAzVs-nlWYtgS5HDA7Um6G3z8vUvv1o'
#
# bot = telebot.TeleBot(token)
# user = User()
# import requests
#
# @bot.message_handler(commands=['start'])
# def handle_start(message):
#     bot.send_message('1001320202352', 'hello')
#     bot.send_message(message.chat.id, "hrllo")
#
#
# bot.infinity_polling()
# api_token = '5043105684:AAEHWAzVs-nlWYtgS5HDA7Um6G3z8vUvv1o'
#
# requests.get('https://api.telegram.org/bot{}/sendMessage'.format(api_token), params=dict(
#    chat_id='1001320202352',
#    text='Hello world!'
# ))