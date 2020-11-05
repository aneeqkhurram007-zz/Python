print("\tPrime Numbers: ")
x = int(input("Enter the upper limit of prime number: "))
print("Prime numbers are: ")
i = 2
while i <= x:
    check = False
    k = 2
    while k < i:
        if i % k == 0:
            check = True
            break
        k += 1
    if check == False:
        print(i)
    i += 1
