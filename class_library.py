
class User:
    def __init__(self):
        self.region = None # название региона, который укажет пользователь
        self.roadToThePlace = None #дорого то места захоронения
        self.nameOfTheDeceased = None # имя умершого
        self.birthDay = None # дата рождения умершого
        self.photoGrave = None # фотография моглиы
        self.doHelp = False # если ты можешь помочь
        self.needHelp = False # Если тебе нужна помощь
        self.wayToHelp = None # способ помочь

    # метод класса, который обновляет все поля до значений по умолчанию
    def update(self):
        self.region = None
        self.roadToThePlace = None
        self.nameOfTheDeceased = None
        self.birthDay = None
        self.photoGrave = None
        self.help = None
        self.wayToHelp = None




