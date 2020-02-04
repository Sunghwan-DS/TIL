def puzzle(start_y, start_x):
    global y, x
    y1 = start_y
    y2 = start_y
    x1 = start_x
    x2 = start_x
    while arr[y1][x1] == 1:
        y1 += 1
    y1 -= 1
    while arr[y1][x1] == 1:
        x1 += 1
    x1 -= 1

    while arr[y2][x2] == 1:
        x2 += 1
    x2 -= 1
    while arr[y2][x2] == 1:
        y2 += 1
    y2 -= 1

    end_y = max(y1, y2)
    end_x = max(x1, x2)

    if y1 == y2:
        d = 0
    elif x1 == x2:
        d = 3
    elif x1 > x2:
        d = 2
    else:
        d = 1

    zero_count = 0
    for i in range(start_y, end_y+1):
        for j in range(start_x, end_x+1):
            if arr[i][j] == 0:
                zero_count += 1
    if zero_count != y*x:
        return


    if d == 0 or d == 2:
        if end_x - start_x != u-1:
            return


    elif d == 1 or d == 3:
        if end_y - start_y != u-1:
            return



N = int(input())
u, v, w, x, y = map(int,input().split())
square = []

arr = []
for i in range(N):
    arr.append(list(map(int,input().split())))


for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            puzzle(i, j)

print(len(square))
for _ in square:
    print(*_)