def move_R(y, x, dir):
    global TF_R, new
    ny = y + dy[dir]
    nx = x + dx[dir]

    while arr[ny][nx] == '.':
        ny += dy[dir]
        nx += dx[dir]
    if arr[ny][nx] == 'O':
        TF_R = True
    else:
        ny -= dy[dir]
        nx -= dx[dir]
        new[ny][nx] = 'R'


def move_B(y, x, dir):
    global TF_B, new
    ny = y + dy[dir]
    nx = x + dx[dir]

    while arr[ny][nx] == '.':
        ny += dy[dir]
        nx += dx[dir]
    if arr[ny][nx] == 'O':
        TF_B = True
    else:
        ny -= dy[dir]
        nx -= dx[dir]
        new[ny][nx] = 'R'


def who(dir, y_R, x_R, y_B, x_B):
    global TF, new
    new[y_R][x_R] = '.'
    new[y_B][x_B] = '.'

    if dir == 0:
        if y_R >= y_B:
            move_R(y_R, x_R, dir)
            move_B(y_B, x_B, dir)

        else:
            move_B(y_B, x_B, dir)
            move_R(y_R, x_R, dir)

    elif dir == 1:
        if x_R >= x_B:
            move_R(y_R, x_R, dir)
            move_B(y_B, x_B, dir)
        else:
            move_B(y_B, x_B, dir)
            move_R(y_R, x_R, dir)

    elif dir == 2:
        if y_R <= y_B:
            move_R(y_R, x_R, dir)
            move_B(y_B, x_B, dir)
        else:
            move_B(y_B, x_B, dir)
            move_R(y_R, x_R, dir)

    elif dir == 3:
        if x_R <= x_B:
            move_R(y_R, x_R, dir)
            move_B(y_B, x_B, dir)
        else:
            move_B(y_B, x_B, dir)
            move_R(y_R, x_R, dir)


    if TF_B:
        return

    elif TF_R:
        TF = True
        return


def order(idx, lst):
    global N, y_R, x_R, y_B, x_B, TF_R, TF_B, TF, ans, new
    if idx == 10:
        new = [arr[_][:] for _ in range(N)]
        TF_R = False
        TF_B = False
        TF = False
        cnt = 0
        for dir in lst:
            who(dir, y_R, x_R, y_B, x_B)
            cnt += 1
            if TF:
                if ans == -1 or ans > cnt:
                    ans = cnt
        return

    for dir in range(4):
        lst.append(dir)
        order(idx+1, lst)
        lst.pop()


N, M = map(int,input().split())
arr = [list(input()) for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
ans = -1


for i in range(N):
    for j in range(M):
        if arr[i][j] == "R":
            y_R = i
            x_R = j
        if arr[i][j] == "B":
            y_B = i
            x_B = j

order(0, [])

print(ans)
