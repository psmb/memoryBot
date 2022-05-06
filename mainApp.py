from telebot import types
import os
import telebot
from dotenv import load_dotenv
from User import User
from backButtonMarkup import backButtonMarkup
from backAndSkipButtonMarkup import backAndSkipButtonMarkup


load_dotenv()


token = os.environ['TOKEN']
channel_id = os.environ['CHANNEL_ID']
bot = telebot.TeleBot(token)


user = User()  # экземпляр класса User, который хранит в себе введенную пользователм информацию


@bot.message_handler(commands=['start'])
def start(message):
    Markup = types.ReplyKeyboardMarkup(row_width=2)
    Btn_1 = types.KeyboardButton('Помочь')
    Btn_2 = types.KeyboardButton('Попросить помощи')
    Markup.add(Btn_1, Btn_2)
    bot.send_message(
        message.chat.id, "Вы готовы помочь с уходом за могилой или хотите попросить о помощи?", reply_markup=Markup)


# Обработчик выбора, который был сделан в start. Функция принимает либо текстовые сообщеие либо фото
@bot.message_handler(content_types=['text', 'photo'])
def main(message):
    # Если пользователь выбрал 'Попросить помощи, то поле needHelp объекта user становиться True.
    if message.text == 'Попросить помощи':
        user.needHelp = True
        chooseRegionForNeedHelp(message)  # Вызывется функция с выбором региона

    if message.text == 'Помочь':  # Если пользователь выбрал 'Помочь', то поле doHelp объекта user становиться True
        user.doHelp = True
        chooseRegionForDoHelp(message)  # Вызывется функция с выбором региона


# =================== FUNCTIONS FOR NEED HELP==================================

# 2)-----------------------
def chooseRegionForNeedHelp(message):
    mesg = bot.send_message(
        message.chat.id, 'В каком регионе находится место памяти?', reply_markup=backButtonMarkup)

    def handler(message):
        if message.text == 'Назад':
            user.needHelp = False  # поле needHelp объекта user заменяется на False
            message.text = None  # текст сообщениея становиться None
            start(message)
        else:
            if message.text != None:  # проверка на значение None
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
            if message.text != None:
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
            coverExpenses(message)
    bot.register_next_step_handler(mesg, handler)


# 8)------------------
def coverExpenses(message):
    if message.text != None:
        user.coverExpenses = message.text

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
            postToChannel(message)
    bot.register_next_step_handler(mesg, handler)


# ===================================================================

# =================== FUNCTIONS FOR DO HELP==================================

# 1)-----------
def chooseRegionForDoHelp(message):
    if message.text != None:
        user.doHelp = True
    mesg = bot.send_message(
        message.chat.id, 'В какой области вы можете помогать?', reply_markup=backButtonMarkup)

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
    print(message.text)

    Markup = types.ReplyKeyboardMarkup(row_width=True)
    Markup.add(types.KeyboardButton('Принести цветы'),
               types.KeyboardButton('Убраться'),
               types.KeyboardButton('Помолиться'),
               types.KeyboardButton('Подключить по видеосвязи'),
               types.KeyboardButton('Другое'),
               types.KeyboardButton('Назад'))
    mesg = bot.send_message(
        message.chat.id, 'Как вы можете помочь?', reply_markup=Markup)

    def handler(message):
        if message.text == 'Назад':
            user.wayToHelp = False
            message.text = None
            chooseRegionForDoHelp(message)
        else:
            selectionOptions = ['Найти могилу', 'Принести цветы', 'Убраться', 'Помолиться',
                                'Подключить по видеосвязи', 'Другое']
            # если пользователь указал вариант, которого нету, то его перенаправит обратно к выбору вариантов
            if selectionOptions.count(message.text) == 0:
                bot.send_message(
                    message.chat.id, 'Такого варианта нету. Пожалуйста, выбирите из предложанных варинтов')
                waysToHelp(message)
            else:
                if message.text == 'Другое':  # если ползьователь выбрал вариант 'Другое', то вызовется функция other
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
    Restart = types.KeyboardButton('Начать сначала')
    Markup.add(Restart)
    if user.doHelp == True:
        mes = "Могу помочь\n" + 'Регион: #' + user.region + '\n' + 'Я могу помочь: ' + user.wayToHelp + '\n' + \
            'Предложил помощь: ' + \
            str(message.from_user.first_name) + '\n' + \
            '\n' + 'Опубикованно через: @pomyani_menya_bot'
        bot.send_message(channel_id, mes)
        bot.send_message(
            message.chat.id, 'Ваше сообщение опубликовано чате @pomyani_menya. Вы можете поискать людей, которым требуется помощь', reply_markup=Markup)

    if user.needHelp == True:
        mes = 'Нужна помощь\n' + 'Регион: #' + user.region + '\n' + 'Как добраться: ' + user.roadToThePlace + '\n' + 'Имя умершого: ' + user.nameOfTheDeceased + '\n' + \
            ('Что нужно сделать: ' + user.whatNeedsToBeDone + '\n' + '\n') if user.whatNeedsToBeDone else "" + \
            'Дата рождения: ' + user.birthDay + '\n' + '\n' + \
            'Опубликовал: ' + str(message.from_user.first_name) + '\n' + \
            '\n' + 'Опубикованно через: @pomyani_menya_bot'
        if user.photoGrave:
            bot.send_photo(channel_id, user.photoGrave, mes)
        else:
            bot.send_message(channel_id, mes)
        mesg = bot.send_message(
            message.chat.id, 'Ваша просьба была опубликована в канале @pomyani_menya. Вы можете сами поискать людей, которые готовы помогать в вашем регионе', reply_markup=Markup)

        def handler(message):
            if message.text == 'Начать сначала':
                user.update()
                start(message)
        bot.register_next_step_handler(mesg, handler)

    user.update()  # обнавляются все поля класса user до значений по умолчанию


if __name__ == '__main__':
    bot.polling()
