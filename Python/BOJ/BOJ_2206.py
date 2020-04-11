# 2020.03.09
# 14:48 ~ 15:34
# BFS 구현
# 시간:5084ms, 코드 길이:810B

N, M = map(int,input().split())
arr = [list(input()) for _ in range(N)]
visited = [[-1] * M for _ in range(N)]

if N == 1 and M == 1:
    print(1)
    exit()

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

q = [(0, 0, 1)]
visited[0][0] = 1
cnt = 1
while q:
    cnt += 1
    for i in range(len(q)):
        y, x, k = q.pop(0)
        for dir in range(4):
            ny = y + dy[dir]
            nx = x + dx[dir]
            if ny == N-1 and nx == M-1:
                print(cnt)
                exit()

            if 0 <= ny <= N-1 and 0 <= nx <= M-1 and visited[ny][nx] < k:
                if arr[ny][nx] == "0":
                    visited[ny][nx] = k
                    q.append((ny, nx, k))
                elif k == 1:
                    visited[ny][nx] = 0
                    q.append((ny, nx, 0))
print(-1)