def merge(array1, size1, array2, size2, array3, size):
    i = 0
    j = 0
    while i < size1:
        array3[i] = array1[i]
        i += 1
    while j < size2:
        array3[i] = array2[j]
        i += 1
        j += 1
    i = 0
    j = 0
    while i < size:
        j = j+i
        while j < size:
            if array3[i] == array3[j]:
                k = j
                while k < size:
                    array3[k] = array3[k+1]
                    k += 1
                size -= 1
            else:
                j += 1
        i += 1

    temp = 0
    for i in range(0, size):
        for j in range(0, size):
            if array3[j] > array3[j+1]:
                temp = array3[j]
                array3[j] = array3[j+1]
                array3[j+1] = temp


size1 = int(input("Enter size for 1st array: "))
array1 = [0]*size1
for i in range(0, size1):
   # num = int(input("Enter "+str(i+1)+" element of 1st array: "))
    array1[i] = int(input("Enter "+str(i+1)+" element of 1st array: "))

size2 = int(input("Enter size for 2nd array: "))
array2 = [0]*size2
for i in range(0, size2):
    array2[i] = int(input("Enter "+str(i+1)+" element of 2nd array: "))

print("Array 1: ")
for i in range(0, size1):
    print(str(array1[i])+" ")
print("Array 2: ")
for i in range(0, size2):
    print(str(array2[i])+" ")
size = size1+size2
array3 = [0]*(size)
merge(array1, size1, array2, size2, array3, size)
print("Array3: ")
for i in range(0, size):
    print(array3[i])
