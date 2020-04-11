def DFS(y, x):
    global cnt
    queue = [[y,x]]
    while queue:
        current = queue.pop(-1)
        for dir in range(4):
            ny = current[0] + dy[dir]
            nx = current[1] + dx[dir]
            if 0 <= ny <= M-1 and 0 <= nx <= N-1 and not visited[ny][nx] and arr[ny][nx] == 0:
                visited[ny][nx] = True
                cnt += 1
                queue.append([ny,nx])


M, N, K = map(int,input().split())
arr = [[0] * N for _ in range(M)]
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

for _ in range(K):
    x1, y1, x2, y2 = map(int,input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            arr[i][j] = 1

visited = [[False] * N for _ in range(M)]
result_lst = []
for i in range(M):
    for j in range(N):
        if arr[i][j] == 0 and not visited[i][j]:
            visited[i][j] = True
            cnt = 1
            DFS(i, j)
            result_lst.append(cnt)
result_lst.sort()

print(len(result_lst))
print(*result_lst)