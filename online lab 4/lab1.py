n1 = int(input("Enter a number 1: "))
n2 = int(input("Enter a number 2: "))
while n1 % n2 != 0:
    n2 = n1
    n1 = int(input("Enter a numebr 1: "))
print("They are dividing each other.")
