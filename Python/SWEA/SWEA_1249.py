from collections import deque

def BFS(y, x):
    q = deque()
    q.append((y, x))

    while q:
        y, x = q.popleft()
        for dy, dx in ((1, 0), (0, -1), (-1, 0), (0, 1)):
            ny = y + dy
            nx = x + dx

            if 0 <= ny < N and 0 <= nx < N:
                if visited[ny][nx] == -1:
                    visited[ny][nx] = visited[y][x] + arr[ny][nx]
                    q.append((ny, nx))
                else:
                    if visited[y][x] + arr[ny][nx] < visited[ny][nx]:
                        visited[ny][nx] = visited[y][x] + arr[ny][nx]
                        q.append((ny, nx))


for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, list(input()))) for _ in range(N)]
    visited = [[-1] * N for _ in range(N)]
    visited[0][0] = 0
    BFS(0, 0)
    print("#%d"%(tc), visited[N-1][N-1])