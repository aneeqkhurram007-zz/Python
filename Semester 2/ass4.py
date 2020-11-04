
def val(x):
    while x <= 0:
        print("You enterd wrong value. ")
        x = int(input("Try Again: "))
    return x


def menu():
    print("Press 1 for Multiplication")
    print("Press 2 for Combination")
    print("Press 3 for Permutation")
    print("Press -1 for Exit")


def mult(x, y):
    return x*y


def factorial(x):
    i = 1
    factorial = 1
    while i <= x:
        factorial = factorial*i
        i = i+1
    return factorial


def comb(x, y):
    return factorial(x)/(factorial(y)*factorial(x-y))


def perm(x, y):
    return factorial(x)/factorial(x-y)


x = int(input("Enter value for x: "))
x = val(x)
y = int(input("Enter value for y: "))
y = val(y)
menu()
choice = int(input("Enter your choice: "))
while choice != -1:
    if choice == 1:
        print("Multiplication is " + str(mult(x, y)))
    elif choice == 2:
        print("Combination is: "+str(int(comb(x, y))))
    elif choice == 3:
        print("Permutation is: "+str(int(perm(x, y))))
    else:
        print("You entered wrong choice.")
    choice = int(input("Enter your choice: "))
