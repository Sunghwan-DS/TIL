def go():
    global R, C, arr, up, down
    new = [[0] * C for _ in range(R)]

    for y in range(R):
        for x in range(C):
            if arr[y][x] >= 5:
                val = (arr[y][x] // 5)
                for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny <= R-1 and 0 <= nx <= C-1 and (ny, nx) not in [(up, 0), (down, 0)]:
                        new[ny][nx] += val
                        arr[y][x] -= val
                new[y][x] += arr[y][x]

            else:
                new[y][x] += arr[y][x]

    arr = new


def clean(up, down):
    global R, C
    for i in range(up-1, 0, -1):
        arr[i][0] = arr[i-1][0]

    for j in range(C-1):
        arr[0][j] = arr[0][j+1]

    for i in range(up):
        arr[i][C-1] = arr[i+1][C-1]

    for j in range(C-1, 0, -1):
        arr[up][j] = arr[up][j-1]


    for i in range(down+1, R-1):
        arr[i][0] = arr[i+1][0]

    for j in range(C-1):
        arr[R-1][j] = arr[R-1][j+1]

    for i in range(R-1, down, -1):
        arr[i][C-1] = arr[i-1][C-1]

    for j in range(C-1, 0, -1):
        arr[down][j] = arr[down][j-1]


R, C, T = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(R)]

for i in range(R):
    if arr[i][0] == -1:
        up = i
        break

down = up+1
arr[up][0] = 0
arr[down][0] = 0

for t in range(T):
    go()
    clean(up, down)

ans = 0

for i in range(R):
    for j in range(C):
        ans += arr[i][j]

print(ans)