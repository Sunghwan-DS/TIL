def move(y, x, dirc):
    ny = y + dy[dirc]
    nx = x + dx[dirc]
    distance = 0
    while arr[ny][nx] == '.':
        distance += 1
        ny += dy[dirc]
        nx += dx[dirc]
    if arr[ny][nx] == 'O':
        return ny, nx, distance
    else:
        return ny - dy[dirc], nx - dx[dirc], distance


def BFS(Ry, Rx, By, Bx):
    q = [(Ry, Rx, By, Bx)]
    visited[Ry][Rx][By][Bx] = True
    cnt = 1
    while q and cnt <= 10:
        for i in range(len(q)):
            Ry, Rx, By, Bx = q.pop(0)
            for dirc in range(4):
                nRy, nRx, R_move = move(Ry, Rx, dirc)
                nBy, nBx, B_move = move(By, Bx, dirc)

                if arr[nBy][nBx] == 'O':
                    continue
                elif arr[nRy][nRx] == 'O':
                    return cnt
                else:
                    if nRy == nBy and nRx == nBx:
                        if R_move > B_move:
                            nRy -= dy[dirc]
                            nRx -= dx[dirc]
                        else:
                            nBy -= dy[dirc]
                            nBx -= dx[dirc]

                        if not visited[nRy][nRx][nBy][nBx]:
                            visited[nRy][nRx][nBy][nBx] = True
                            q.append((nRy, nRx, nBy, nBx))
                    else:
                        if not visited[nRy][nRx][nBy][nBx]:
                            visited[nRy][nRx][nBy][nBx] = True
                            q.append((nRy, nRx, nBy, nBx))
        cnt += 1
    return -1


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

N, M = map(int,input().split())
arr = [list(input()) for _ in range(N)]
visited = [[[[False]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'B':
            By = i
            Bx = j
            arr[i][j] = '.'
        elif arr[i][j] == 'R':
            Ry = i
            Rx = j
            arr[i][j] = '.'

print(BFS(Ry, Rx, By, Bx))