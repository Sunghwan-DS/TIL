# 2020.03.09
# 17:05 ~ 18:10
# 시뮬레이션, DFS 구현
# pypy:2156ms, 코드 길이:2323B

def DFS(Ry, Rx, By, Bx, idx):
    global ans
    if ans <= idx or idx == 11:
        return

    if arr[Ry][Rx] == "O":
        if arr[By][Bx] == "O":
            return
        else:
            ans = min(ans, idx)
            return

    if arr[By][Bx] == "O":
        return


    if Ry >= By:
        new_Ry, new_Rx = move(Ry, Rx, 2, By, Bx)
        new_By, new_Bx = move(By, Bx, 2, new_Ry, new_Rx)
        DFS(new_Ry, new_Rx, new_By, new_Bx, idx + 1)

        new_By, new_Bx = move(By, Bx, 0, Ry, Rx)
        new_Ry, new_Rx = move(Ry, Rx, 0, new_By, new_Bx)
        DFS(new_Ry, new_Rx, new_By, new_Bx, idx + 1)

    else:
        new_By, new_Bx = move(By, Bx, 2, Ry, Rx)
        new_Ry, new_Rx = move(Ry, Rx, 2, new_By, new_Bx)
        DFS(new_Ry, new_Rx, new_By, new_Bx, idx + 1)

        new_Ry, new_Rx = move(Ry, Rx, 0, By, Bx)
        new_By, new_Bx = move(By, Bx, 0, new_Ry, new_Rx)
        DFS(new_Ry, new_Rx, new_By, new_Bx, idx + 1)


    if Rx >= Bx:
        new_Ry, new_Rx = move(Ry, Rx, 1, By, Bx)
        new_By, new_Bx = move(By, Bx, 1, new_Ry, new_Rx)
        DFS(new_Ry, new_Rx, new_By, new_Bx, idx + 1)

        new_By, new_Bx = move(By, Bx, 3, Ry, Rx)
        new_Ry, new_Rx = move(Ry, Rx, 3, new_By, new_Bx)
        DFS(new_Ry, new_Rx, new_By, new_Bx, idx + 1)

    else:
        new_By, new_Bx = move(By, Bx, 1, Ry, Rx)
        new_Ry, new_Rx = move(Ry, Rx, 1, new_By, new_Bx)
        DFS(new_Ry, new_Rx, new_By, new_Bx, idx + 1)

        new_Ry, new_Rx = move(Ry, Rx, 3, By, Bx)
        new_By, new_Bx = move(By, Bx, 3, new_Ry, new_Rx)
        DFS(new_Ry, new_Rx, new_By, new_Bx, idx + 1)


def move(y, x, dir, other_y, other_x):
    ny = y + dy[dir]
    nx = x + dx[dir]
    while arr[ny][nx] == "." and not (ny == other_y and nx == other_x):
        ny += dy[dir]
        nx += dx[dir]
    if arr[ny][nx] == "O":
        return ny, nx
    else:
        return ny - dy[dir], nx - dx[dir]


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

N, M = map(int,input().split())
arr = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == "B":
            By = i
            Bx = j
        elif arr[i][j] == "R":
            Ry = i
            Rx = j

arr[By][Bx] = "."
arr[Ry][Rx] = "."

ans = 20
DFS(Ry, Rx, By, Bx, 0)
if ans == 20:
    print(-1)
else:
    print(ans)