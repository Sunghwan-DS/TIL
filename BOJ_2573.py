# 2020.02.27
# 13:10 ~ 13: 38
# 탐색 구현
# 시간:PyPy 692ms, 코드 길이:1353B

def check(y, x):
    global N, M
    cnt = 1
    visited = [[False] * M for _ in range(N)]
    visited[y][x] = True

    s = [(y, x)]

    while s:
        y, x = s[-1]

        for dir in range(4):
            ny = y + dy[dir]
            nx = x + dx[dir]

            if not visited[ny][nx] and arr[ny][nx] != 0:
                s.append((ny,nx))
                visited[ny][nx] = True
                cnt += 1
                break

        else:
            s.pop()
    return cnt


N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
melt = [[0] * M for _ in range(N)]
dy = [-1, 0 , 1, 0]
dx = [0, 1, 0, -1]

ice = []
for i in range(N):
    for j in range(M):
        if arr[i][j] != 0:
            ice.append((i, j))

ans = 0
cnt = 0
while ice:
    if len(ice) != check(ice[0][0], ice[0][1]):
        ans = cnt
        break
    cnt += 1

    for i in range(len(ice) - 1, -1, -1):
        y, x = ice[i]
        m = 0

        for dir in range(4):
            ny = y + dy[dir]
            nx = x + dx[dir]

            if arr[ny][nx] == 0:
                melt[y][x] += 1

    for i in range(len(ice) - 1, -1, -1):
        y, x = ice[i]
        if arr[y][x] - melt[y][x] <= 0:
            arr[y][x] = 0
            ice.pop(i)
        else:
            arr[y][x] -= melt[y][x]

        melt[y][x] = 0

print(ans)