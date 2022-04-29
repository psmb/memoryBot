import telebot


from class_library import User
from telebot import types
token = '5043105684:AAEHWAzVs-nlWYtgS5HDA7Um6G3z8vUvv1o'

bot = telebot.TeleBot(token)


user = User()# экземпляр класса User, который хранит в себе введенную пользователм информацию

def CreateBackButton():# фунция, которя создает кнопку "Назад"
    Markup = types.ReplyKeyboardMarkup(row_width=True)
    BackBtn = types.KeyboardButton('Назад')
    Markup.add(BackBtn)
    return Markup


def CreateButton_WaysToHelp():# функция, которая создает клавиотуру с выбором вариантов помощи. Вызывается в WaysToHelp
    Markup = types.ReplyKeyboardMarkup(row_width=True)
    Btn_1 = types.KeyboardButton('Принести цветы')
    Btn_2 = types.KeyboardButton('Убраться')
    Btn_3 = types.KeyboardButton('Помолиться')
    Btn_4 = types.KeyboardButton('Подключить по видеосвязи')
    Btn_5 = types.KeyboardButton('Другое')
    BackBtn = types.KeyboardButton('Назад')
    Markup.add(Btn_1, Btn_2, Btn_3, Btn_4, Btn_5, BackBtn)
    return Markup


def CreateChooseMarkup():# функция, которая создает клавиотуру с выбором нужды. Вызывается в handle_start
    Markup = types.ReplyKeyboardMarkup(row_width=2)
    Btn_1 = types.KeyboardButton('Помочь')
    Btn_2 = types.KeyboardButton('Попросить помощи')
    Markup.add(Btn_1, Btn_2)
    return Markup


#стартовая функция. Тут пользователь указывает, что ему нужно. Дальше идет разветление  взависимости от того, что он выбрал: 'Поросить помощи' или же 'Помочь'
@bot.message_handler(commands=['start'])
def handle_start(message):
    Markup = CreateChooseMarkup()#-функция, которая создает клавиотуру с выбором нужды
    bot.send_message(message.chat.id, "Вы готовы помочь с уходом за могилой или хотите попросить о помощи?", reply_markup=Markup)
    print('/start')
    print(user.__dict__)


#Обработчик выбора, который был сделан в handle_start. Функция принимает либо текстовые сообщеие либо фото
@bot.message_handler(content_types=['text', 'photo'])
def main(message):
   if message.text == 'Попросить помощи':#Если пользователь выбрал 'Попросить помощи, то поле needHelp объекта user становиться True.
        user.needHelp = True
        chooseRegionForNeedHelp(message)# Вызывется функция с выбором региона

   if message.text == 'Помочь': #Если пользователь выбрал 'Помочь', то поле doHelp объекта user становиться True
       user.doHelp = True
       chooseRegionForDoHelp(message)# Вызывется функция с выбором региона



#=================== FUNCTIONS FOR NEED HELP==================================

# 2)-----------------------
#Функция с выбором региона
def chooseRegionForNeedHelp(message):
    Markup = CreateBackButton()#фунция, которя создает кнопку "Назад"
    print(user.__dict__)
    mesg = bot.send_message(message.chat.id, 'Выбор области', reply_markup=Markup)
    bot.register_next_step_handler(mesg, CheckToNeedBack_handle_start)


#Функция проверяет, нужно ли пользователю вернуться на шаг назад (выбор нужды). Если текст сообщение  message.text - 'Назад', то 1 - поле needHelp объекта user заменяется на False
# 2 - текст сообщениея становиться None. 3 - вызывается функция handle_start, которая предоставляет возможность выбрать нужду. Если текст сообщения != 'Назад',
# то вызывается следующая функция - roadToRegion
def CheckToNeedBack_handle_start(message):
    if message.text == 'Назад':
        user.needHelp = False #поле needHelp объекта user заменяется на False
        message.text = None #текст сообщениея становиться None
        handle_start(message) #функция handle_start, которая предоставляет возможность выбрать нужду
    else:
        roadToRegion(message)  #вызывается следующая функция - roadToRegion



# 3)--------------------
# Функция с указанием региона
def roadToRegion(message):
    print(message.text)
    # поскольку в эту функцию могу вернутья из следующей - nameOfTheDeceased, то текст сообщения message.text может быть равен None и, что бы нее допустить записи в
    #поле класса region объекта user значения None, идет проверка и только в случаее, если текст сообщения message.text != None, то допускается запись введенного ползьзователем сообщения
    if message.text != None:# проверка на значение None
        user.region = message.text # добавление введенного пользователем текста (регион) в поле region класса  user
    mesg = bot.send_message(message.chat.id, 'Опишите как добраться до места памяти')
    print(user.__dict__)
    bot.register_next_step_handler(mesg, CheckToNeedBack_ChooseRegionForNeedHelp)

# Проверка, нужно ли пользователю вернуться на шаг назад. Логика используется та же, что и в CheckToNeedBack_handle_start
def CheckToNeedBack_ChooseRegionForNeedHelp(message):
    if message.text == 'Назад':
        user.region = None
        message.text = None
        chooseRegionForNeedHelp(message) # вызов предыдущий функции
    else:
        nameOfTheDeceased(message) # вызов следующий функции






#4)------------------------------
#функция с выбором именнем умершгого
def nameOfTheDeceased(message):
    if message.text != None:# логика та же, что и в roadToRegion
        user.roadToThePlace = message.text #добавление введенного пользователем текста (дорога до места памяти) в поле roadToThePlace класса  user
    mesg = bot.send_message(message.chat.id, 'Имя кого вы хотите помянуть')
    print(user.__dict__)
    bot.register_next_step_handler(mesg, CheckNeedToBack_RoadToRegion)


# Проверка, нужно ли пользователю вернуться на шаг назад. Логика используется та же, что и в CheckToNeedBack_handle_start
def CheckNeedToBack_RoadToRegion(message):
    if message.text == 'Назад':
        user.roadToThePlace = None
        message.text = None
        roadToRegion(message)# вызов предыдущий функции
    else:
        birthDay(message) #вызов следующий функции



#5)------------------------
#функция с указанием даты рождения умершгого
def birthDay(message):
    if message.text != None:# логика та же, что и в roadToRegion
        user.nameOfTheDeceased = message.text #добавление введенного пользователем текста (имени умершгого) в поле  nameOfTheDeceased класса user
    mesg = bot.send_message(message.chat.id, 'Дата рождения того, кого вы хотите помянуть')
    print(user.__dict__)
    bot.register_next_step_handler(mesg, CheckNeedToBack_NameOfTheDeceased)

# Проверка, нужно ли пользователю вернуться на шаг назад. Логика используется та же, что и в CheckToNeedBack_handle_start
def CheckNeedToBack_NameOfTheDeceased(message):
    if message.text == 'Назад':
        user.nameOfTheDeceased = None
        message.text = None
        nameOfTheDeceased(message)# вызов предыдущий функции
    else:
        gravePhoto(message)#вызов следующий функции


#6)------------------
#функция добавления фотографии могилы.Логика используется та же, что и
def gravePhoto(message):
    print(message.text)
    if message.text != None:# логика та же, что и в roadToRegion
        user.birthDay = message.text #добавление введенного пользователем текста (даты рождения умершого) в поле birthDay  класса user
    mesg = bot.send_message(message.chat.id, 'Фото могилы')
    print(user.__dict__)
    bot.register_next_step_handler(mesg, CheckNeedToBack_BirthDay)

# Проверка, нужно ли пользователю вернуться на шаг назад. Логика используется та же, что и в CheckToNeedBack_handle_start
def CheckNeedToBack_BirthDay(message):
    if message.text == 'Назад':
        user.birthDay = None
        message.text = None
        birthDay(message)# вызов предыдущий функции
    else:
        addGravePhoto(message)#вызов следующий функции

#функция, которая 1. добавляет в поле photoGrave класса User фото могилы. 2. вызывает функцию публикации сообщения
def addGravePhoto(message):
    user.photoGrave = message.text
    addToTheChat(message)






#===================================================================

#=================== FUNCTIONS FOR DO HELP==================================

#1)-----------
#функция выбора региона
def chooseRegionForDoHelp(message):
    Markup = CreateBackButton()# функцию, которая создает кнопу 'Назад'
    if message.text != None:# логика та же, что и в roadToRegion
        user.doHelp = True
    mesg = bot.send_message(message.chat.id, 'Выбор области', reply_markup=Markup)
    # print(user.__dict__)
    bot.register_next_step_handler(mesg, CheckNeedToBack_HandleStart)


# Проверка, нужно ли пользователю вернуться на шаг назад. Логика используется та же, что и в CheckToNeedBack_handle_start
def CheckNeedToBack_HandleStart(message):
    if message.text == 'Назад':
        user.doHelp = False
        message.text = None
        handle_start(message)# вызов предыдущий функции
    else:
        waysToHelp(message)#вызов следующий функции


#2)-------------------------
#функцию предостовляет варианты помощи
def waysToHelp(message):
    print(message.text)
    if message.text != None:# логика та же, что и в roadToRegion
        user.region = message.text #добавление текста сообщений (регион) в поле region класса user
    Markup = CreateButton_WaysToHelp()# функция создает клавиатуру с вариантами помощи
    mesg = bot.send_message(message.chat.id, 'Как вы можете помочь?', reply_markup=Markup)
    print(user.__dict__)
    bot.register_next_step_handler(mesg, CheckNeedToBack_ChooseRegionForDoHelp)


# Проверка, нужно ли пользователю вернуться на шаг назад. Логика используется та же, что и в CheckToNeedBack_handle_start
def CheckNeedToBack_ChooseRegionForDoHelp(message):
    if message.text == 'Назад':
        user.wayToHelp = False
        message.text = None
        chooseRegionForDoHelp(message)# вызов предыдущий функции
    else:
        handlerChoose(message)#вызов следующий функции

#3)--------------------------------------
#обработчик выбора варианта помщи
def handlerChoose(message):
    print(message.text)
    selectionOptions = ['Найти могилу', 'Принести цветы', 'Убраться', 'Помолиться',
                            'Подключить по видеосвязи', 'Другое']
    if selectionOptions.count(message.text) == 0:#если пользователь указал вариант, которого нету, то его перенаправит обратно к выбору вариантов
        bot.send_message(message.chat.id, 'Такого варианта нету. Пожалуйста, выбирите из предложанных варинтов')
        waysToHelp(message)
    else:
        if message.text == 'Другое':#если ползьователь выбрал вариант 'Другое', то вызовется функция other
            other(message)
        else:
            user.wayToHelp = message.text #добавление текста сообщений (выбранный вариант помощи) wayToHelp в поле  класса user
            addToTheChat(message) # вызов функции, которая публикует сообщение


#добавляет другой вариант помощи, который укажет пользователь в свободном поле ввода
def other(message):
    Markup = CreateBackButton()# создание кнопки "Назад'
    mesg = bot.send_message(message.chat.id, 'Опишите пожалуйста, как именно вы можете помочь', reply_markup=Markup)
    user.wayToHelp = message.text#  #добавление текста сообщений (указанный ползтователем в свободном поле вариант помощи) wayToHelp в поле  класса user
    print(user.__dict__)
    bot.register_next_step_handler(mesg, CheckNeedToBack_WaysToHelp)

# Проверка, нужно ли пользователю вернуться на шаг назад. Логика используется та же, что и в CheckToNeedBack_handle_start
def CheckNeedToBack_WaysToHelp(message):
    if message.text == 'Назад':
        user.wayToHelp = False
        message.text = None
        waysToHelp(message)# вызов предыдущий функции
    else:
        addToTheChat(message)#вызов следующий функции







#===========================================================================================
#функция публикации сообщения в общий чат
def addToTheChat(message):
    bot.send_message(message.chat.id, ' Ваше сообщение опубликовано в чате Таком-то, мы можете поискать людей, которым требуется помощь в')
    print(user.__dict__)
    user.update()# обнавляются все поля класса user до значений по умолчанию
    print(user.__dict__)






# @bot.message_handler(commands=['start'])
# def handle_start(message):
#     InlineMarkup = types.InlineKeyboardMarkup(row_width=True)
#     InlineBtn1 = types.InlineKeyboardButton('Помочь', callback_data='Do Help')
#     InlineBtn2 = types.InlineKeyboardButton('Поросить помощи', callback_data='Need Help')
#     InlineMarkup.add(InlineBtn1, InlineBtn2)
#     bot.send_message(message.chat.id, "Вы готовы помочь с уходом за могилой или хотите попросить о помощи?", reply_markup=InlineMarkup)
#     InlineBtn1 = types.ReplyKeyboardRemove()
#     InlineBtn2 = types.Rem
#     print(message.text)
#
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback_handler(call):
#     bot.answer_callback_query(call.id)
#     if call.data == 'Do Help':
#         chooseRegionForDoHelp(call.message)
#     if call.data == 'Need Help':
#         chooseRegionForDoHelp(call.message)
#
#
#
# @bot.message_handler(content_types=['text', 'photo'])
# def main(callback):
#     if callback.data == 'Do Help':
#         chooseRegionForDoHelp(callback.message)
#     if callback.data == 'Need Help':
#         bot.send_message(callback.message.chat.id, 'vbcbcvbcb')









bot.infinity_polling()





