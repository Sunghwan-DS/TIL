def BFS(start):
    q = [start]
    cnt = 0
    visited = [[False] * N for _ in range(N)]
    visited[start[0]][start[1]] = True
    while q:
        cnt += 1
        for _ in range(len(q)):
            y, x = q.pop(0)

            for dirc in range(4):
                ny = y + dy[dirc]
                nx = x + dx[dirc]
                if 0 <= ny <= N-1 and 0 <= nx <= N-1 and not visited[ny][nx] and arr[ny][nx] != 1:
                    if arr[ny][nx] == 2:
                        return cnt // 2 + cnt % 2
                    visited[ny][nx] = True
                    q.append((ny, nx))


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)
ans = 100
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            ans = min(ans, BFS((i, j)))

print(ans)