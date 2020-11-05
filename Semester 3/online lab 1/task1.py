print("\tTables")
while True:
    x = int(input("Enter a number: "))
    for i in range(1, 11):
        print(str(x)+" "+"X"+" " + str(i) + " "+"="+" "+str(x*i))
    choice = input("Do you want to continue: ")
    if choice != 'y':
        break
