# 2020.03.09
# 17:05 ~ 18:10
# 시뮬레이션, BFS 구현
# 시간:60ms, 코드 길이:3823B

def BFS(Ry, Rx, By, Bx):
    q = [(Ry, Rx, By, Bx)]
    visited[Ry][Rx][By][Bx] = True
    cnt = 0
    while q and cnt <= 10:
        for i in range(len(q)):
            Ry, Rx, By, Bx = q.pop(0)
            if arr[Ry][Rx] == "O":
                if arr[By][Bx] == "O":
                    continue
                else:
                    print(cnt)
                    exit()

            if arr[By][Bx] == "O":
                continue


            if Ry >= By:
                new_Ry, new_Rx = move(Ry, Rx, 2, By, Bx)
                new_By, new_Bx = move(By, Bx, 2, new_Ry, new_Rx)
                if not visited[new_Ry][new_Rx][new_By][new_Bx]:
                    visited[new_Ry][new_Rx][new_By][new_Bx] = True
                    q.append((new_Ry, new_Rx, new_By, new_Bx))

                new_By, new_Bx = move(By, Bx, 0, Ry, Rx)
                new_Ry, new_Rx = move(Ry, Rx, 0, new_By, new_Bx)
                if not visited[new_Ry][new_Rx][new_By][new_Bx]:
                    visited[new_Ry][new_Rx][new_By][new_Bx] = True
                    q.append((new_Ry, new_Rx, new_By, new_Bx))

            else:
                new_By, new_Bx = move(By, Bx, 2, Ry, Rx)
                new_Ry, new_Rx = move(Ry, Rx, 2, new_By, new_Bx)
                if not visited[new_Ry][new_Rx][new_By][new_Bx]:
                    visited[new_Ry][new_Rx][new_By][new_Bx] = True
                    q.append((new_Ry, new_Rx, new_By, new_Bx))

                new_Ry, new_Rx = move(Ry, Rx, 0, By, Bx)
                new_By, new_Bx = move(By, Bx, 0, new_Ry, new_Rx)
                if not visited[new_Ry][new_Rx][new_By][new_Bx]:
                    visited[new_Ry][new_Rx][new_By][new_Bx] = True
                    q.append((new_Ry, new_Rx, new_By, new_Bx))


            if Rx >= Bx:
                new_Ry, new_Rx = move(Ry, Rx, 1, By, Bx)
                new_By, new_Bx = move(By, Bx, 1, new_Ry, new_Rx)
                if not visited[new_Ry][new_Rx][new_By][new_Bx]:
                    visited[new_Ry][new_Rx][new_By][new_Bx] = True
                    q.append((new_Ry, new_Rx, new_By, new_Bx))

                new_By, new_Bx = move(By, Bx, 3, Ry, Rx)
                new_Ry, new_Rx = move(Ry, Rx, 3, new_By, new_Bx)
                if not visited[new_Ry][new_Rx][new_By][new_Bx]:
                    visited[new_Ry][new_Rx][new_By][new_Bx] = True
                    q.append((new_Ry, new_Rx, new_By, new_Bx))

            else:
                new_By, new_Bx = move(By, Bx, 1, Ry, Rx)
                new_Ry, new_Rx = move(Ry, Rx, 1, new_By, new_Bx)
                if not visited[new_Ry][new_Rx][new_By][new_Bx]:
                    visited[new_Ry][new_Rx][new_By][new_Bx] = True
                    q.append((new_Ry, new_Rx, new_By, new_Bx))

                new_Ry, new_Rx = move(Ry, Rx, 3, By, Bx)
                new_By, new_Bx = move(By, Bx, 3, new_Ry, new_Rx)
                if not visited[new_Ry][new_Rx][new_By][new_Bx]:
                    visited[new_Ry][new_Rx][new_By][new_Bx] = True
                    q.append((new_Ry, new_Rx, new_By, new_Bx))

        cnt += 1

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
visited = [[[[False]*10 for _ in range(10)] for _ in range(10)] for _ in range(10)]

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

BFS(Ry, Rx, By, Bx)
print(-1)