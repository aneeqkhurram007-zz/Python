
i = 1
count = 1
sum = 0
while i <= 99:
    if count % 2 == 0:
        sum = sum-1/i
    if count % 2 != 0:
        sum = sum+1/i
    i += 2
    count += 1
print(sum)
pie = 4*sum
print("The value of pi is: "+str(format(pie, '.4f')))
