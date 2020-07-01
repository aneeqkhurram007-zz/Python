
i = 1
sum1 = 0
sum2 = 0
num = int(input("Enter any number: "))

while i <= num:

    sum1 = sum1 + i
    i += 1

print("\nSum without formula : " + str(sum1))
sum2 = (num * (num + 1)) / 2
print("\nSum with formula : " + str((int(sum2))))
if sum1 == sum2:
    print("\nBoth are same")

else:
    print("\nBoth are different")
