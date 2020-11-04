
def mul(x, y):
    return x*y


def comb(x, y):
    return factorial(x)/factorial(y)*factorial(x-y)


def perm(x, y):
    return factorial(x)/factorial(x-y)


def factorial(x):
    if x <= 0:
        return 1
    else:
        return x*factorial(x-1)


x = int(input("Value for X: "))
y = int(input("Value for Y: "))
char = input("Please enter option (1,2,3): ")
print("You entered "+char)
if char == '1':
    print("Multiplication is: "+str(int(mul(x, y))))
elif char == '2':
    print("Combination is: "+str(int(comb(x, y))))
elif char == '3':
    print("Permiability is:"+str(int(perm(x, y))))
