class User:
    def __init__(self):
        self.update()

    # метод класса, который обновляет все поля до значений по умолчанию
    def update(self):
        self.region = None
        self.roadToThePlace = None
        self.nameOfTheDeceased = None
        self.birthDay = None
        self.photoGrave = None
        self.doHelp = False
        self.needHelp = False
        self.thank = False
        self.thankMessage = False
        self.thankPhoto = False
        self.wayToHelp = None
        self.whatNeedsToBeDone = None
        self.coverExpenses = False
