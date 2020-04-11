# 2020.03.12
# 18:55 ~ 19:11
# BFS, 시뮬레이션 구현
# 시간:60ms, 코드 길이:1244B

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            y = i
            x = j

arr[y][x] = 0
size = 2
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
visited = [[False] * N for _ in range(N)]
q = [(y, x)]
time = 0
fish = 0
ans = 0
cnt = 0
while q:
    eat = []
    for i in range(len(q)):
        y, x = q.pop(0)
        for dir in range(4):
            ny = y + dy[dir]
            nx = x + dx[dir]

            if 0 <= ny <= N-1 and 0 <= nx <= N-1 and not visited[ny][nx] and arr[ny][nx] <= size:
                visited[ny][nx] = True
                q.append((ny, nx))
                if 0 < arr[ny][nx] < size:
                    eat.append((ny,nx))
    cnt += 1

    if eat:
        eat_y, eat_x = 21, 21
        for ey, ex in eat:
            if eat_y > ey:
                eat_y, eat_x = ey, ex
            elif eat_y == ey:
                eat_x = min(eat_x, ex)
        arr[eat_y][eat_x] = 0
        q = [(eat_y, eat_x)]
        visited = [[False] * N for _ in range(N)]
        visited[eat_y][eat_x] = True
        fish += 1
        ans += cnt
        cnt = 0

        if fish == size:
            fish = 0
            size += 1

print(ans)