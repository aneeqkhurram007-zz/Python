class student:
    passLimit = 33
    listOfCourse = []
    listOfQuiz = []

    @classmethod
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def __init__(self, name, listOfCourse, listOfQuiz):
        self.name = name
        self.listOfCourse = listOfCourse
        self.listOfQuiz = listOfQuiz

    def printInfo(self):
        print("\nName of a Student: "+self.name)
        print("\nCourse Data:")
        for x in self.listOfCourse:
            print(x)
        print("\nQuiz Data:")
        for x in self.listOfQuiz:
            print(x)

    def dropCourse(self, course):
        self.listOfCourse.remove(course)

    def regCourse(self, course):
        self.listOfCourse.insert(course)

    def getListOfQuiz(self):
        return self.listOfQuiz

    @staticmethod
    def getPassedQuizzes(self, listOfQuiz):
        count = 0
        for x in listOfQuiz:
            if int(x) > self.passLimit:
                count += 1
        return count
