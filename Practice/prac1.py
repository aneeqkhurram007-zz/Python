# Task 1 put sum of first 50 terms
sum = 1
i = 0
while (i < 50):
    sum = sum+4
    i = i+1
print("So the sum for task 1 is: "+str(sum))

# Task 2 read a character.
x = str(input("Enter a character: "))
i = 0
while(i < 10):
    print(x)
    i += 1

# Task 4 sum of 1 + 4 + 7 + ..... + 148

sum = 0
i = 1
while(i <= 148):
    sum += i
    i += 3
print("So the sum for task 4 is: "+str(sum))

# Task 5 sum of 100 + 95 + 90 + .... + 5

sum = 0
i = 100
while(i >= 5):
    sum += i
    i -= 5
print("So the sum for task 5 is: "+str(sum))
