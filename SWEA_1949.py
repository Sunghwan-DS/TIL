def DFS(y, x, deep, k):
    global K, ans
    visited[y][x] = True

    for dir in range(4):
        ny = y + dy[dir]
        nx = x + dx[dir]

        if 0 <= ny <= N-1 and 0 <= nx <= N-1 and not visited[ny][nx]:
            if arr[ny][nx] < arr[y][x]:
                DFS(ny, nx, deep+1, k)

            elif k and arr[ny][nx] - K < arr[y][x]:
                pre = arr[ny][nx]
                arr[ny][nx] = arr[y][x] - 1
                DFS(ny, nx, deep+1, 0)
                arr[ny][nx] = pre

    else:
        ans = max(ans, deep)

    visited[y][x] = False


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
for tc in range(1, int(input())+1):
    N, K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    highest = []
    max_height = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > max_height:
                max_height = arr[i][j]
                highest = [(i, j)]
            elif arr[i][j] == max_height:
                highest.append((i, j))
    ans = 0

    for y, x in highest:
        visited = [[False] * N for _ in range(N)]
        DFS(y, x, 1, 1)

    print("#%d"%(tc), ans)