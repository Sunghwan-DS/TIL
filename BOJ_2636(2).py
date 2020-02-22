# 2020.02.22
# 08:44 ~ 09:03
# DFS, BFS 구현
# 시간:72ms, 코드 길이: 1298B

def Find_air(y, x):
    s = [(y,x)]
    visited[y][x] = True
    while s:
        y, x = s[-1]
        for dir in range(4):
            ny = y + dy[dir]
            nx = x + dx[dir]

            if 0 <= ny <= N-1 and 0 <= nx <= M-1 and not visited[ny][nx]:
                if arr[ny][nx] == 0:
                    s.append((ny, nx))
                    visited[ny][nx] = True
                    break

                elif arr[ny][nx] == 1:
                    q.append((ny, nx))
                    visited[ny][nx] = True
                    continue

        else:
            s.pop()


N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
q = []

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
time = 0
last_cheese = 0

Find_air(0, 0)

while q:
    time += 1
    last_cheese = len(q)
    for i in range(len(q)):
        y, x = q.pop(0)

        for dir in range(4):
            ny = y + dy[dir]
            nx = x + dx[dir]

            if 0 <= ny <= N-1 and 0 <= nx <= M-1 and not visited[ny][nx]:
                if arr[ny][nx] == 1:
                    q.append((ny,nx))
                    visited[ny][nx] = True

                elif arr[ny][nx] == 0:
                    Find_air(ny, nx)

print(time)
print(last_cheese)