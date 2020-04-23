# 알고리즘 틀림
# 5
# 0 0 0 1 0
# 0 0 1 0 1
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0

def issafe(val):
    global N
    if 0 <= val <= N-1:
        return True
    else:
        return False


def check(y, x):
    global N
    for dirc in range(4):
        ny, nx = y, x
        while issafe(ny + by[dirc]) and issafe(nx + bx[dirc]):
            ny += by[dirc]
            nx += bx[dirc]
            if fix[ny][nx]:
                return False
    fix[y][x] = True
    return True


dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
by = [-1, -1, 1, 1]
bx = [-1, 1, -1, 1]

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
fix = [[False] * N for _ in range(N)]
y, x = 0, 0
ans = 0
dirc = 0

while True:
    visited[y][x] = True
    if arr[y][x]:
        if check(y, x):
            ans += 1
    if issafe(y + dy[dirc]) and issafe(x + dx[dirc]) and not visited[y + dy[dirc]][x + dx[dirc]]:
        y += dy[dirc]
        x += dx[dirc]
        continue
    else:
        dirc = (dirc + 1) % 4
        if issafe(y + dy[dirc]) and issafe(x + dx[dirc]) and not visited[y + dy[dirc]][x + dx[dirc]]:
            y += dy[dirc]
            x += dx[dirc]
            continue
        else:
            break
for i in range(N):
    print(*fix[i])
print(ans)