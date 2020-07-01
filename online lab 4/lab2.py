n1 = 1
n2 = 1
print(str(n1)+"\n"+str(n2))
n3 = n1+n2
while n3 < 30000:
    if n3 >= 30000:
        break
    print(n3)
    n1 = n2
    n2 = n3
    n3 = n1+n2
