from date import *

day = int(input("Enter new Date: "))
month = int(input("Enter new Month: "))
year = int(input("Enter new Year: "))
d1 = Date(day, month, year)
print(d1)
d2 = d1
print(d2)
d2.setMonth(3)
print(d2)
print(d1)
