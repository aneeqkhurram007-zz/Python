def checkWin(array):
    if array[0] == array[1] and array[1] == array[2]:
        if array[0] != 0 and array[1] != 0 and array[2] != 0:
            return 1
    if array[3] == array[4] and array[4] == array[5]:
        if array[3] != 0 and array[4] != 0 and array[5] != 0:
            return 1
    if array[6] == array[7] and array[7] == array[8]:
        if array[6] != 0 and array[7] != 0 and array[8] != 0:
            return 1
    if array[0] == array[3] and array[3] == array[6]:
        if array[0] != 0 and array[3] != 0 and array[6] != 0:
            return 1
    if array[1] == array[4] and array[4] == array[7]:
        if array[1] != 0 and array[4] != 0 and array[7] != 0:
            return 1
    if array[2] == array[5] and array[5] == array[8]:
        if array[2] != 0 and array[5] != 0 and array[8] != 0:
            return 1
    if array[0] == array[4] and array[4] == array[8]:
        if array[0] != 0 and array[4] != 0 and array[8] != 0:
            return 1
    if array[2] == array[4] and array[4] == array[6]:
        if array[2] != 0 and array[4] != 0 and array[6] != 0:
            return 1
    return 0


print("\t__0__|__1__|__2__")
print("\t__3__|__4__|__5__")
print("\t  6  |  7  |  8  ")
array = [0]*10
print("'O' marks for player 1: ")
print("'X' marks for player 2: ")
for i in range(0, 9):
    if i % 2 == 0:
        print("Player 1 turns: ")
        position = int(input("Position you want to place your move: "))
        if array[position] == 0:
            array[position] = 'O'
            flag1 = checkWin(array)
            if flag1 == 1:
                break
        else:
            print("Already filled Try Again.")
            i = i-1
    else:
        print("Player 2 turns: ")
        position = int(input("Position you want to place your move: "))
        if array[position] == 0:
            array[position] = 'X'
            flag2 = checkWin(array)
            if flag2 == 1:
                break
        else:
            print("Already filled Try Again.")
            i = i-1
    i = i+1
if flag1 == flag2:
    print("Match Draw")
elif flag2 == 0 and flag1 == 1:
    print("Player'O' wins: ")
elif flag1 == 0 and flag2 == 1:
    print("Player'X' wins: ")
for i in range(0, 9):
    if array[i] == 0:
        array[i] = ' '
    i = i+1
i = 0
r = 0

while r < 3:
    if r == 2:
        print("\t  " + str(array[i]) + "  |  " +
              str(array[i + 1]) + "  |  " + str(array[i + 2]))
    else:
        print("\t__" + str(array[i]) + "__|__" +
              str(array[i + 1]) + "__|__" + str(array[i + 2]) + "__")
    i = i+3
    r = r+1
