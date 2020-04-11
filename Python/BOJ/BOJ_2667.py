# 2020.02.21
# 10:06 ~ 10:15
# BFS 구현
# 시간:60ms, 코드 길이:724B

def BFS(y, x):
    q = [(y, x)]
    cnt = 0
    while q:
        y, x = q.pop(0)
        visited[y][x] = True
        cnt += 1

        for dir in range(4):
            ny = y + dy[dir]
            nx = x + dx[dir]

            if 0 <= ny <= N-1 and 0 <= nx <= N-1 and not visited[ny][nx] and arr[ny][nx] == '1':
                q.append((ny, nx))
                visited[ny][nx] = True
    ans.append(cnt)


N = int(input())
arr = [input() for _ in range(N)]
visited = [[False] * N for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
ans = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == '1' and not visited[i][j]:
            BFS(i, j)

ans.sort()
print(len(ans))
for num in ans:
    print(num)