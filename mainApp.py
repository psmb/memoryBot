from telebot import types
import os
import telebot
# from dotenv import load_dotenv
from User import User
from backButtonMarkup import backButtonMarkup
from backAndSkipButtonMarkup import backAndSkipButtonMarkup


# load_dotenv()


token = os.environ['TOKEN']
channel_id = os.environ['CHANNEL_ID']
bot = telebot.TeleBot(token)


user = User()  # экземпляр класса User, который хранит в себе введенную пользователм информацию


@bot.message_handler(commands=['start'])
def start(message):
    Markup = types.ReplyKeyboardMarkup(row_width=2)
    Markup.add(types.KeyboardButton('Помочь'),
               types.KeyboardButton('Попросить помощи'),
               types.KeyboardButton('Поблагодарить'))
    bot.send_message(
        message.chat.id, "Вы готовы помочь с уходом за могилой или хотите попросить о помощи?", reply_markup=Markup)


# Обработчик выбора, который был сделан в start. Функция принимает либо текстовые сообщеие либо фото
@bot.message_handler(content_types=['text', 'photo'])
def main(message):
    if message.text == 'Попросить помощи':
        user.needHelp = True
        chooseRegionForNeedHelp(message)

    if message.text == 'Помочь':
        user.doHelp = True
        chooseRegionForDoHelp(message)

    if message.text == 'Поблагодарить':
        user.thank = True
        thank(message)


# =================== FUNCTIONS FOR NEED HELP==================================

# 2)-----------------------
def chooseRegionForNeedHelp(message):
    mesg = bot.send_message(
        message.chat.id, 'В каком регионе находится место памяти?', reply_markup=backButtonMarkup)

    def handler(message):
        if message.text == 'Назад':
            user.needHelp = False
            message.text = None
            start(message)
        else:
            if message.text != None:
                user.region = message.text
            roadToRegion(message)
    bot.register_next_step_handler(mesg, handler)


# 3)--------------------
def roadToRegion(message):
    mesg = bot.send_message(
        message.chat.id, 'Опишите как добраться до места памяти', reply_markup=backButtonMarkup)

    def handler(message):
        if message.text == 'Назад':
            user.region = None
            message.text = None
            chooseRegionForNeedHelp(message)
        else:
            if message.text != None:
                user.roadToThePlace = message.text
            nameOfTheDeceased(message)
    bot.register_next_step_handler(mesg, handler)

# Проверка, нужно ли пользователю вернуться на шаг назад. Логика используется та же, что и в CheckToNeedBack_handle_start


# 4)------------------------------
# функция с выбором именнем умершгого
def nameOfTheDeceased(message):
    mesg = bot.send_message(
        message.chat.id, 'Имя кого вы хотите помянуть', reply_markup=backButtonMarkup)

    def handler(message):
        if message.text == 'Назад':
            user.roadToThePlace = None
            message.text = None
            roadToRegion(message)
        else:
            if message.text != None:
                user.nameOfTheDeceased = message.text
            birthDay(message)
    bot.register_next_step_handler(mesg, handler)


# 5)------------------------
# функция с указанием даты рождения умершгого
def birthDay(message):
    mesg = bot.send_message(
        message.chat.id, 'Дата рождения того, кого вы хотите помянуть', reply_markup=backAndSkipButtonMarkup)

    def handler(message):
        if message.text == 'Назад':
            user.nameOfTheDeceased = None
            message.text = None
            nameOfTheDeceased(message)
        else:
            if message.text != None and message.text != 'Пропустить':
                user.birthDay = message.text
            gravePhoto(message)
    bot.register_next_step_handler(mesg, handler)

# Проверка, нужно ли пользователю вернуться на шаг назад. Логика используется та же, что и в CheckToNeedBack_handle_start


# 6)------------------
# функция добавления фотографии могилы.Логика используется та же, что и
def gravePhoto(message):
    mesg = bot.send_message(
        message.chat.id, 'Фото могилы', reply_markup=backAndSkipButtonMarkup)

    def handler(message):
        if message.text == 'Назад':
            user.birthDay = None
            message.text = None
            birthDay(message)
        else:
            if message.photo != None:
                user.photoGrave = message.photo[-1].file_id
            whatNeedsToBeDone(message)
    bot.register_next_step_handler(mesg, handler)


# 7)------------------
def whatNeedsToBeDone(message):
    mesg = bot.send_message(
        message.chat.id, 'Что нужно сделать?', reply_markup=backButtonMarkup)

    def handler(message):
        if message.text == 'Назад':
            user.whatNeedsToBeDone = None
            message.text = None
            whatNeedsToBeDone(message)
        else:
            user.whatNeedsToBeDone = message.text
            coverExpenses(message)
    bot.register_next_step_handler(mesg, handler)


# 8)------------------
def coverExpenses(message):
    Markup = types.ReplyKeyboardMarkup(row_width=2)
    Markup.add(types.KeyboardButton('Да'), types.KeyboardButton('Нет'))
    mesg = bot.send_message(
        message.chat.id, 'Готовы ли вы оплатить расходы?', reply_markup=Markup)

    def handler(message):
        if message.text == 'Назад':
            user.coverExpenses = None
            message.text = None
            coverExpenses(message)
        else:
            if message.text == 'Да':
                user.coverExpenses = True
            postToChannel(message)
    bot.register_next_step_handler(mesg, handler)


# ===================================================================

# =================== FUNCTIONS FOR DO HELP==================================

# 1)-----------
def chooseRegionForDoHelp(message):
    if message.text != None:
        user.doHelp = True
    mesg = bot.send_message(
        message.chat.id, 'В каком регионе вы можете помогать?', reply_markup=backButtonMarkup)

    def handler(message):
        if message.text == 'Назад':
            user.doHelp = False
            message.text = None
            start(message)
        else:
            if message.text != None:
                user.region = message.text
            waysToHelp(message)
    bot.register_next_step_handler(mesg, handler)


# 2)-------------------------
def waysToHelp(message):
    Markup = types.ReplyKeyboardMarkup(row_width=2)
    Markup.add(types.KeyboardButton('🌺 Принести цветы'),
               types.KeyboardButton('🧹 Убраться'),
               types.KeyboardButton('🙏🏻 Помолиться'),
               types.KeyboardButton('🎥 Подключить по видеосвязи'),
               types.KeyboardButton('✍🏻 Другое'),
               types.KeyboardButton('🔙 Назад'))
    mesg = bot.send_message(
        message.chat.id, 'Как вы можете помочь?', reply_markup=Markup)

    def handler(message):
        if message.text == 'Назад':
            user.wayToHelp = False
            message.text = None
            chooseRegionForDoHelp(message)
        else:
            if message.text == 'Другое':
                mesg = bot.send_message(
                    message.chat.id, 'Опишите пожалуйста, как именно вы можете помочь', reply_markup=backButtonMarkup)

                def handler(message):
                    if message.text == 'Назад':
                        user.wayToHelp = False
                        message.text = None
                        waysToHelp(message)
                    else:
                        user.wayToHelp = message.text
                        postToChannel(message)
                bot.register_next_step_handler(mesg, handler)

            else:
                user.wayToHelp = message.text
                postToChannel(message)

    bot.register_next_step_handler(mesg, handler)


# 3)--------------------------------------
# обработчик выбора варианта помщи


# Проверка, нужно ли пользователю вернуться на шаг назад. Логика используется та же, что и в CheckToNeedBack_handle_start


# ===========================================================================================
# функция публикации сообщения в общий чат
def postToChannel(message):
    Markup = types.ReplyKeyboardMarkup(row_width=True)
    Markup.add(types.KeyboardButton('Начать сначала'))

    if user.doHelp == True:
        mes = f"""
*Могу помочь*
🌍 Регион: \#{user.region}
🎯 Я могу: {user.wayToHelp}
📞 Опубликовал: @{str(message.from_user.username)}

Опубикованно через: @pomyani\_menya\_bot
"""

        bot.send_message(channel_id, mes, parse_mode="MarkdownV2")
        bot.send_message(
            message.chat.id, '✅ Ваше сообщение опубликовано в канале @pomyani_menya. Вы можете поискать людей, которым требуется помощь', reply_markup=Markup)

    if user.needHelp == True:
        mes = f"""
*Нужна помощь*
🌍 Регион: \#{user.region}
🚕 Как добраться: {user.roadToThePlace}
👤 Имя умершого: {user.nameOfTheDeceased}
📅 Дата рождения умершего: {user.birthDay}
🎯 Что нужно сделать: {user.whatNeedsToBeDone}
{'💰 Я готов покрыть расходы' if user.coverExpenses else ''}
📞 Опубликовал: @{str(message.from_user.username)}

📮 Опубикованно через: @pomyani\_menya\_bot
"""

        if user.photoGrave:
            bot.send_photo(channel_id, user.photoGrave,
                           mes, parse_mode="MarkdownV2")
        else:
            bot.send_message(channel_id, mes, parse_mode="MarkdownV2")

        mesg = bot.send_message(
            message.chat.id, '✅ Ваша просьба была опубликована в канале @pomyani_menya. Вы можете сами поискать людей, которые готовы помогать в вашем регионе', reply_markup=Markup)

        def handler(message):
            if message.text == 'Начать сначала':
                user.update()
                start(message)
        bot.register_next_step_handler(mesg, handler)

    user.update()


# 4)--------------------------------------
# обработчик выбора варианта благодарности

def thank(message):
    mesg = bot.send_message(
        message.chat.id, 'Если через @pomyani_menya_bot вы нашли людей, которые смогли прийти на могилу ваших родственников в другом городе, расскажите об этом и поблагодарите их.', reply_markup=backButtonMarkup)

    def handler(message):
        if message.text == 'Назад':
            user.thankMessage = None
            message.text = None
            start(message)
        else:
            if message.text != None:
                user.thankMessage = message.text
            thankPhoto(message)
    bot.register_next_step_handler(mesg, handler)


def thankPhoto(message):
    mesg = bot.send_message(
        message.chat.id, 'Добавьте фото', reply_markup=backAndSkipButtonMarkup)

    def handler(message):
        if message.text == 'Назад':
            user.thankMessage = None
            message.text = None
            thank(message)
        else:
            if message.photo != None:
                user.thankPhoto = message.photo[-1].file_id
            postThank(message)
    bot.register_next_step_handler(mesg, handler)


def postThank(message):
    Markup = types.ReplyKeyboardMarkup(row_width=True)
    Markup.add(types.KeyboardButton('Начать сначала'))

    mes = f"""
*Благодарность*
✍🏻 {user.thankMessage}
📞 Опубликовал: @{str(message.from_user.username)}

Опубикованно через: @pomyani\_menya\_bot
"""

    if user.thankPhoto:
        bot.send_photo(channel_id, user.thankPhoto,
                       mes, parse_mode="MarkdownV2")
    else:
        bot.send_message(channel_id, mes, parse_mode="MarkdownV2")

    mesg = bot.send_message(
        message.chat.id, '✅ Ваша благодарность была опубликована в канале @pomyani_menya', reply_markup=Markup)

    def handler(message):
        if message.text == 'Начать сначала':
            user.update()
            start(message)
    bot.register_next_step_handler(mesg, handler)


if __name__ == '__main__':
    bot.polling()
