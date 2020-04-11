# 2020.04.05
# 21:58 ~ 22:38
# BFS라고 해놓고 DFS 구현하여 망함
# 안돌려봤지만 아마도 시간초과

def BFS(idx, Ry, Rx, By, Bx):
    global ans, N, M
    if idx >= ans:
        return

    if idx == 11:
        return

    for dirc in range(4):
        nRy = Ry + dy[dirc]
        nRx = Rx + dx[dirc]
        R_move = 0
        while arr[nRy][nRx] == '.':
            R_move += 1
            nRy += dy[dirc]
            nRx += dx[dirc]

        nBy = By + dy[dirc]
        nBx = Bx + dx[dirc]
        B_move = 0
        while arr[nBy][nBx] == '.':
            B_move += 1
            nBy += dy[dirc]
            nBx += dx[dirc]

        if arr[nRy][nRx] == 'O' and arr[nBy][nBx] != 'O':
            ans = min(ans, idx)
            return

        elif arr[nBy][nBx] == 'O':
            return

        nRy -= dy[dirc]
        nRx -= dx[dirc]
        nBy -= dy[dirc]
        nBx -= dx[dirc]

        if nRy == nBy and nRx == nBx:
            if R_move > B_move:
                nRy -= dy[dirc]
                nRx -= dx[dirc]
            else:
                nBy -= dy[dirc]
                nBx -= dx[dirc]
            BFS(idx+1, nRy, nRx, nBy, nBx)
        else:
            BFS(idx + 1, nRy, nRx, nBy, nBx)


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

N, M = map(int,input().split())
arr = [list(input()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'B':
            By, Bx = i, j
            arr[i][j] = '.'
        elif arr[i][j] == 'R':
            Ry, Rx = i, j
            arr[i][j] = '.'

ans = 11
BFS(1, Ry, Rx, By, Bx)
if ans == 11:
    print(-1)
else:
    print(ans)
