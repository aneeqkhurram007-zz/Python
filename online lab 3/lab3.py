num1 = int(input("Enter a number 1: "))
num2 = int(input("Enter a number 2: "))
while num1 % num2 != 0:
    print("They are not dividing each other.")
    num1 = int(input("Try Again for number 1:"))
    num2 = int(input("Try Again for number 2:"))
print("They are dividing each other.")
