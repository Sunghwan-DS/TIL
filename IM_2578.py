def checking(i, j):
    if max(field[i]) == 0:
        y[i] = 1
    for _ in range(5):
        if field[_][j] != 0:
            break
    else:
        x[j] = 1

    if i==j:
        for _ in range(5):
            if field[_][_] != 0:
                break
        else:
            yx[0] = 1

    if i + j == 4:
        for _ in range(5):
            if field[0+_][4-_] != 0:
                break
        else:
            yx[1] = 1
    return sum(x) + sum(y) + sum(yx)


field = []
y = [0, 0, 0, 0, 0]
x = [0, 0, 0, 0, 0]
yx = [0, 0]
for _ in range(5):
    field.append(list(map(int,input().split())))

number = []
for _ in range(5):
    line = list(map(int,input().split()))
    for __ in range(5):
        number.append(line[__])

for idx, num in enumerate(number):
    next_num = False
    for i in range(5):
        for j in range(5):
            if num == field[i][j]:
                field[i][j] = 0
                if checking(i, j) >= 3:
                    print(idx+1)
                    exit()
                next_num = True
                break
        if next_num:
            break