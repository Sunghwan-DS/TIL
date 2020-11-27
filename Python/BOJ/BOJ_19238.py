# 2020.11.27
# 14:05 ~ 15:17

from collections import deque

N, M, F = map(int, input().split())
field = []
for _ in range(N):
    row = list(map(int, input().split()))
    field.append(row)

ty, tx = map(int, input().split())
ty -= 1
tx -= 1

info = {}
order = [[0] * N for _ in range(N)]
for _ in range(M):
    sy, sx, ey, ex = map(int, input().split())
    info[(sy - 1, sx - 1)] = (ey - 1, ex - 1)
    order[sy - 1][sx - 1] = 1

dy = (-1, 0, 1, 0)
dx = (0, -1, 0, 1)


def find_customer(ty, tx, F):
    if order[ty][tx]:
        return ty, tx, F

    q = deque()
    q.append((ty, tx, 0))

    visited = [[False] * N for _ in range(N)]
    visited[ty][tx] = True

    target = []
    while q:
        for _ in range(len(q)):
            y, x, cnt = q.popleft()
            remain = F - (cnt + 1)
            if remain < 0:
                return -1, -1, -1
            for dirc in range(4):
                ny = y + dy[dirc]
                nx = x + dx[dirc]

                if 0 <= ny < N and 0 <= nx < N and not field[ny][nx] and not visited[ny][nx]:
                    if order[ny][nx]:
                        visited[ny][nx] = True
                        target.append((ny, nx, cnt + 1))
                    else:
                        visited[ny][nx] = True
                        q.append((ny, nx, cnt + 1))
        if target:
            target.sort(key=lambda x: (x[0], x[1]))
            ey, ex, cnt = target[0]
            return ey, ex, remain

    return -1, -1, -1


def go(ty, tx, F):
    order[ty][tx] = 0
    ey, ex = info[(ty, tx)]
    del info[(ty, tx)]

    if ey == ty and ex == tx:
        return ty, tx, F

    q = deque()
    q.append((ty, tx, 0))

    visited = [[False] * N for _ in range(N)]
    visited[ty][tx] = True

    while q:
        y, x, cnt = q.popleft()
        remain = F - (cnt + 1)
        if remain < 0:
            return -1, -1, -1

        for dirc in range(4):
            ny = y + dy[dirc]
            nx = x + dx[dirc]

            if 0 <= ny < N and 0 <= nx < N and not field[ny][nx] and not visited[ny][nx]:
                if ny == ey and nx == ex:
                    return ey, ex, F + (cnt + 1)
                else:
                    visited[ny][nx] = True
                    q.append((ny, nx, cnt + 1))

    return -1, -1, -1


while info:
    ty, tx, F = find_customer(ty, tx, F)
    if ty != -1:
        ty, tx, F = go(ty, tx, F)
        if ty == -1:
            break
    else:
        break

if ty == -1:
    print(-1)
else:
    print(F)