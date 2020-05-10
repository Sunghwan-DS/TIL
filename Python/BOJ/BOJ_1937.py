def DFS(y, x):
    global N

    stack = [(y, x)]
    cnt = 0
    while stack:
        y, x = stack[-1]
        for dirc in range(4):
            ny = y + dy[dirc]
            nx = x + dx[dirc]
            if 0 <= ny <= N-1 and 0 <= nx <= N-1 and arr[ny][nx] > arr[y][x]:
                if not DP[ny][nx]:
                    stack.append((ny, nx))
                    cnt = 0
                    break

                elif DP[ny][nx] > 0:
                    cnt = max(cnt, DP[ny][nx])
        else:
            cnt += 1
            DP[y][x] = max(DP[y][x], cnt)
            stack.pop()
    return

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
DP = [[0] * N for _ in range(N)]

dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)
ans = 0

for i in range(N):
    for j in range(N):
        if not DP[i][j]:
            DFS(i, j)

for i in range(N):
    for j in range(N):
        ans = max(ans, DP[i][j])
print(ans)