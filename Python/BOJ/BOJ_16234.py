def BFS(y, x):
    global TF
    q = [[y, x]]
    s = [[y, x]]
    tot = arr[y][x]
    while q:
        current = q.pop(0)
        y = current[0]
        x = current[1]
        for dir in range(4):
            ny = y + dy[dir]
            nx = x + dx[dir]
            if 0 <= ny <= N-1 and 0 <= nx <= N-1 and L <= abs(arr[y][x] - arr[ny][nx]) <= R and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append([ny, nx])
                s.append([ny, nx])
                tot += arr[ny][nx]

    if len(s) == 1:
        return

    TF = True
    avg = tot // len(s)

    for i in s:
        arr[i[0]][i[1]] = avg


N, L, R = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
cnt = -1
TF = True
while TF:
    cnt += 1
    visited = [[False] * N for _ in range(N)]
    TF = False
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                BFS(i,j)

print(cnt)