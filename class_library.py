import telebot
import class_library
from telebot import types
token = ''

bot = telebot.TeleBot(token)

class User:
    def __init__(self):
        self.choose = 'Flase'
        self.state = 'Flase'
        self.region = 'False'
        self.roadToThePlace = 'False'
        self.nameOfTheDeceased = 'False'
        self.birthDay = 'Fasle'
        self.photo = 'False'
        self.canHelp = 'Flse'

