def prime(x):
    flag = 0
    i = 2
    while i <= x/2:
        if x % i == 0:
            flag = 1
            break
        i += 1
    if flag == 1:
        return 1
    else:
        return 0


x = int(input("Enter a number X: "))
y = int(input("Enter a number Y: "))
i = 1
if prime(x) == 0 and prime(y) == 0:
    print("GCD does not exist.")
else:
    while i <= x and i <= y:
        if x % i == 0 and y % i == 0:
            flag = i
        i += 1
    print("GCD is: "+str(flag))
