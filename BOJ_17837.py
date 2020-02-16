def white(y, x, ny, nx, idx):
    a = 999999
    lst = []
    while a != idx:
        a = arr[y][x].pop()
        lst.insert(0, a)

    for num in lst:
        units[num][0] = ny
        units[num][1] = nx
    arr[ny][nx].extend(lst)
    if len(arr[ny][nx]) >= 4:
        print(ans)
        exit()


def red(y, x, ny, nx, idx):
    a = 999999
    lst = []
    while a != idx:
        a = arr[y][x].pop()
        lst.append(a)
    for num in lst:
        units[num][0] = ny
        units[num][1] = nx
    arr[ny][nx].extend(lst)
    if len(arr[ny][nx]) >= 4:
        print(ans)
        exit()


def blue(idx):
    if units[idx][2] == 0:
        units[idx][2] = 1
    elif units[idx][2] == 1:
        units[idx][2] = 0
    elif units[idx][2] == 2:
        units[idx][2] = 3
    elif units[idx][2] == 3:
        units[idx][2] = 2


def move():
    global ans
    ans += 1
    for idx, u in enumerate(units):
        y = u[0]
        x = u[1]
        dir = u[2]

        ny = y + dy[dir]
        nx = x + dx[dir]

        if 0 <= ny <= N-1 and 0 <= nx <= N-1:
            if color[ny][nx] == 0:
                white(y, x, ny, nx, idx)

            elif color[ny][nx] == 1:
                red(y, x, ny, nx, idx)

            elif color[ny][nx] == 2:

                ny = y - dy[dir]
                nx = x - dx[dir]
                blue(idx)
                if not 0 <= ny <= N-1 or not 0 <= nx <= N-1 or color[ny][nx] == 2:
                    pass

                elif 0 <= ny <= N-1 and 0 <= nx <= N-1:
                    if color[ny][nx] == 0:
                        white(y, x, ny, nx, idx)

                    elif color[ny][nx] == 1:
                        red(y, x, ny, nx, idx)

        else:
            ny = y - dy[dir]
            nx = x - dx[dir]
            blue(idx)
            if not 0 <= ny <= N - 1 or not 0 <= nx <= N - 1 or color[ny][nx] == 2:
                pass

            elif 0 <= ny <= N - 1 and 0 <= nx <= N - 1:
                if color[ny][nx] == 0:
                    white(y, x, ny, nx, idx)

                elif color[ny][nx] == 1:
                    red(y, x, ny, nx, idx)

    if ans == 996:
        print(-1)
        exit()
    move()


def minus1(num):
    return num-1


N, K = map(int,input().split())
color = [list(map(int,input().split())) for _ in range(N)]
arr = [[[] for __ in range(N)] for _ in range(N)]
units = [list(map(minus1,map(int,input().split()))) for _ in range(K)]

for idx, i in enumerate(units):
    arr[i[0]][i[1]].append(idx)

dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]
ans = 0

move()