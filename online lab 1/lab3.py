num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
i = num1
sum = 0
while i <= num2:
    if i % 2 == 0:
        sum = sum+i
    i += 1
print("The sum is: "+str(sum))
