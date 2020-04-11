def move(cnt, i, j, direction):
    global field
    if cnt == N**2 + 1:
        return
    field[i][j] = cnt
    if direction == 1:
        if j+1 <= N-1:
            if field[i][j+1] == 0:
                move(cnt+1, i, j+1, 1)
            else:
                move(cnt + 1, i+1, j, 2)
        else:
            move(cnt + 1, i + 1, j, 2)

    elif direction == 2:
        if i+1 <= N - 1:
            if field[i+1][j] == 0:
                move(cnt+1, i+1, j, 2)
            else:
                move(cnt + 1, i, j-1, 3)
        else:
            move(cnt + 1, i, j-1, 3)

    elif direction == 3:
        if j-1 >= 0:
            if field[i][j-1] == 0:
                move(cnt+1, i, j-1, 3)
            else:
                move(cnt + 1, i-1, j, 4)
        else:
            move(cnt + 1, i-1, j, 4)

    elif direction == 4:
        if field[i-1][j] == 0:
            move(cnt+1, i-1, j, 4)
        else:
            move(cnt+1, i, j+1, 1)


T = int(input())
for _ in range(T):
    N = int(input())
    field = [[0] * N for __ in range(N)]
    i = 0
    j = 0
    move(1, 0, 0, 1)
    print("#%d"%(_+1))
    for __ in range(N):
        print(" ".join([str(i) for i in field[__]]))