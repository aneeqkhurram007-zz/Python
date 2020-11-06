class Date(object):
    def __init__(self, *args, **kwargs):
        self.setDay(args[0])
        self.setMonth(args[1])
        self.setyear(args[2])

    def setDay(self, day):
        self.__day = day

    def getDay(self):
        return self.__day

    def setMonth(self, month):
        self.__month = month

    def getMonth(self):
        return self.__month

    def setyear(self, year):
        self._year = year

    def getYear(self):
        return self._year

    def __str__(self):
        return "Date dd/mm/yyyy : "+str(self.getDay())+"/"+str(self.getMonth())+"/"+str(self.getYear())
