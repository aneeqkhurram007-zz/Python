from student import *


def listOfCourse():
    arrayList = []
    print("\nEnter name of your courses: ")
    i = 0
    while i < 5:
        arrayList.insert(i, input())
        i += 1
    return arrayList


def listOfQuiz():
    arrayList = []
    print("Enter your quiz numbers: ")
    i = 0
    while i < numOfQuiz:
        arrayList.insert(i, input())
        while int(arrayList[i]) < 0:
            arrayList.append(input("Try Again. Youe entered invalid value: "))
        i += 1
    return arrayList


numOfStudent = int(input("Enter number of students: "))
numOfQuiz = int(input("\nEnter number of quiz: "))
students = []


i = 0
while i < numOfStudent:
    print("\nEnter data for Student "+str(i+1))
    name = input("\nEnter your name: ")
    students.append(student(name, listOfCourse(), listOfQuiz()))
    i += 1
print("\nStudents Data: ")
for x in students:
    x.printInfo()
    print("Number of Passed Quizzes: " +
          str(student.getPassedQuizzes(x, x.getListOfQuiz())))
