N, M = map(int,input().split())
r, c, dir = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
visited[r][c] = True
ans = 1

while True:
    TF = True
    for d in range(4):
        ny = r + dy[d]
        nx = c + dx[d]
        if 0 <= ny <= N-1 and 0 <= nx <= M-1 and not visited[ny][nx] and arr[ny][nx] == 0:
            TF = False
            break

    if TF:
        ny = r - dy[dir]
        nx = c - dx[dir]
        if not 0 <= ny <= N-1 or not 0 <= nx <= M-1 or arr[ny][nx] == 1:
            break
        else:
            r = ny
            c = nx
            continue

    ny = r + dy[(dir - 1) % 4]
    nx = c + dx[(dir - 1) % 4]

    if arr[ny][nx] == 0 and not visited[ny][nx]:
        visited[ny][nx] = True
        ans += 1
        r = ny
        c = nx

    dir = (dir-1)%4


print(ans)