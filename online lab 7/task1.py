def average(array):
    avg = 0
    print("Marks entered by the user: "+str(array))
    for i in range(0, 10):
        avg = avg + array[i]
    print("Average is: "+str(int(avg/i)))


marks = []
for i in range(0, 10):
    marks.append(int(input("Enter marks for Subject "+str(i+1)+" : ")))
    if marks[i] > 100:
        marks.pop(i)
        marks.append(int(input("Enter marks for Subject "+str(i+1)+" : ")))
average(marks)
