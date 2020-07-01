i = 1
terms = 5
num = int(input("Enter a number: "))
while not(num > 1 and num < 21):
    num = int(input("Enter a number: "))
while i <= terms:
    print(str(num)+" * "+str(i)+" = "+str(num*i))
    if i % 5 == 0:
        print("Prss ESC to exit or any key to continue")
        ch = ord(input("Enter a character: "))
        if ch != 27:
            terms = terms+5
    i = i+1
