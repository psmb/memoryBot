import telebot
import class_library
from telebot import types
token = ''

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def handle_start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    itemBtn1 = types.KeyboardButton('Помочь')
    itemBtn2 = types.KeyboardButton('Поросить помощи')
    markup.add(itemBtn1, itemBtn2)
    bot.send_message(message.chat.id, "Вы готовы помочь с уходом за могилой или хотите попросить о помощи?", reply_markup=markup)
    markup = types.ReplyKeyboardRemove()



@bot.message_handler(content_types=['text', 'photo'])
def main(message):
   if message.text == 'Поросить помощи':
      needHelp(message)
   if message.text == 'Помочь':
       chooseRegionForDoHelp(message)




#=================== FUNCTIONS FOR NEED HELP==================================
#1)
def needHelp(message):
    mesg = bot.send_message(message.chat.id, 'В каком регионе находится место памяти?')
    bot.register_next_step_handler(mesg, chooseRegionForNeedHelp)

# 2)
def chooseRegionForNeedHelp(message):
    mesg = bot.send_message(message.chat.id, 'Выбор области')
    region = message.text
    bot.register_next_step_handler(mesg, roadToRedion)

# 3)
def roadToRedion(message):
    mesg = bot.send_message(message.chat.id, 'Опишите как добраться до места памяти')
    road = message.text
    bot.register_next_step_handler(mesg, nameOfTheDeceased)

#4)
def nameOfTheDeceased(message):
    mesg = bot.send_message(message.chat.id, ' Имя кого вы хотите помянуть')
    nameOfTheMentioned = message.text
    bot.register_next_step_handler(mesg, birthDay)

#5)
def birthDay(message):
    mesg = bot.send_message(message.chat.id, 'Дата рождения того, кого вы хотите помянуть')
    dayOfBirth = message.text
    bot.register_next_step_handler(mesg,gravePhoto)

#6)
def gravePhoto(message):
    mesg = bot.send_message(message.chat.id, 'Фото могилы')
    addToTheChat(message)
#===================================================================

#=================== FUNCTIONS FOR DO HELP==================================

#1)
def chooseRegionForDoHelp(message):
    mesg = bot.send_message(message.chat.id, 'Выбор области')
    region = message.text
    bot.register_next_step_handler(mesg,waysToHelp)

#2)
def waysToHelp(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    itemBtn1 = types.KeyboardButton('Найти могилу')
    itemBtn2 = types.KeyboardButton('Принести цветы')
    itemBtn3 = types.KeyboardButton('Убраться')
    itemBtn4 = types.KeyboardButton('Помолиться')
    itemBtn5 = types.KeyboardButton('Подключить по видеосвязи')
    itemBtn6 = types.KeyboardButton('Другое')
    markup.add(itemBtn1, itemBtn2,itemBtn3,itemBtn4,itemBtn5,itemBtn6)
    mesg = bot.send_message(message.chat.id, 'Как вы можете помочь?',reply_markup=markup)
    markup = types.ReplyKeyboardMarkup()
    print(message.text)
    markup = types.ReplyKeyboardMarkup()
    bot.register_next_step_handler(mesg,handlerChoose)


#3)
def handlerChoose(message):
    print(message.text)
    selectionOptions = ['Найти могилу','Принести цветы','Убраться','Помолиться',
                        'Подключить по видеосвязи', 'Другое']
    if selectionOptions.count(message.text) == 0:
        bot.send_message(message.chat.id, 'Такого варианта нету. Пожалуйста, выбирите из предложанных варинтов')
        waysToHelp(message)
    else:
        if message.text == 'Другое':
            other(message)
        else:
            addToTheChat(message)



def other(message):
    mesg = bot.send_message(message.chat.id, 'Опишите пожалуйста, как именно вы можете помочь')
    bot.register_next_step_handler(mesg,addToTheChat)
#===========================================================================================

def addToTheChat(message):
    bot.send_message(message.chat.id, ' Ваше сообщение опубликовано в чате Таком-то, мы можете поискать людей, которым требуется помощь в')





# @bot.message_handler(content_types=['text'])
# def welcome(message):
#     mesg = bot.send_message(message.chat.id,'Please send me message')
#     bot.register_next_step_handler(mesg, test)
#
# def test(message):
#     mesg = bot.send_message(message.chat.id,'You send me message')
#     bot.register_next_step_handler(mesg, test_2)
#
# def test_2(message):
#     bot.send_message(message.chat.id,'You send me messag2')







bot.infinity_polling()
# import telegram




# bot = TeleBot(token)
#
# @bot.message_handler(content_types=['text'])
# def get_text_messages(message):
#     print(message.from_user.id)
#     if message.text == "Привет":
#         bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
#     elif message.text == "/help":
#         bot.send_message(message.from_user.id, "Напиши привет")
#     else:
#         bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
#
#
# bot.polling(none_stop=True, interval=0)
# print('dqwdwq')