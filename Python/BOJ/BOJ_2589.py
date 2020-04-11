# 2020.02.26
# 16:20 ~ 16:48
# BFS 구현
# 시간:4704ms, 코드 길이:759B

def BFS(y, x):
    global H, W
    visited = [[False] * W for _ in range(H)]
    q = [(y, x)]
    cnt = -1
    visited[y][x] = True
    while q:
        cnt += 1

        for i in range(len(q)):
            y, x = q.pop(0)

            for d in range(4):
                ny = y + dy[d]
                nx = x + dx[d]

                if 0 <= ny <= H-1 and 0 <= nx <= W-1 and not visited[ny][nx] and arr[ny][nx] == 'L':
                    q.append((ny, nx))
                    visited[ny][nx] = True

    return cnt


H, W = map(int, input().split())
arr = [list(input()) for _ in range(H)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
ans = 0

for i in range(H):
    for j in range(W):
        if arr[i][j] == 'L':
            ans = max(ans, BFS(i, j))

print(ans)