def DFS(y, x, rain):
    queue = [[y, x]]
    while queue:
        for _ in range(len(queue)):
            current = queue.pop(-1)
            for dir in range(4):
                ny = current[0] + dy[dir]
                nx = current[1] + dx[dir]
                if 0 <= ny <= N-1 and 0 <= nx <= N-1 and visited[ny][nx] and arr[ny][nx] > rain:
                    visited[ny][nx] = False
                    queue.append([ny,nx])


N = int(input())
arr = []
rain = []
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
for i in range(N):
    arr.append(list(map(int,input().split())))
    for j in range(N):
        if arr[i][j] not in rain:
            rain.append(arr[i][j])
rain.sort()


result = 1
for r in rain:
    visited = [[True] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > r and visited[i][j]:
                cnt += 1
                visited[i][j] = False
                DFS(i,j,r)

    if result < cnt:
        result = cnt

print(result)