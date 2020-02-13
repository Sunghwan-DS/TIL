N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

dy = [0, 1, 0]
dx = [1, 0, -1]

for i in range(N):
    for j in range(M):
        visited = [[False] * M for _ in range(N)]
        visited[i][j] = True
        stack = [(i,j)]
        result = [(i,j)]
        while stack:
            y, x = stack[-1]

            for dir in range(3):
                ny = y + dy[dir]
                nx = x + dx[dir]

                if 0 <= ny <= N-1 and 0 <= nx <= M-1 and not visited[ny][nx]:

