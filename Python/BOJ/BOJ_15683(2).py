# 2020.03.12
# 07:10 ~ 07:38
# DFS, 시뮬레이션 구현
# 시간:844ms, 코드 길이:1798B

def go(idx, now):
    global N, M, ans
    if idx == len(cctv):
        res = 0
        for i in range(N):
            for j in range(M):
                if now[i][j] == 0:
                    res += 1
        ans = min(ans, res)
        return

    y, x, k = cctv[idx]
    if k == 1:
        for dir in range(4):
            new = [now[i][:] for i in range(N)]
            show(new, y, x, dir)
            go(idx+1, new)

    elif k == 2:
        for dir in range(2):
            new = [now[i][:] for i in range(N)]
            show(new, y, x, dir)
            show(new, y, x, dir+2)
            go(idx+1, new)

    elif k == 3:
        for dir in range(4):
            new = [now[i][:] for i in range(N)]
            show(new, y, x, dir)
            show(new, y, x, (dir+1)%4)
            go(idx + 1, new)

    elif k == 4:
        for dir in range(4):
            new = [now[i][:] for i in range(N)]
            show(new, y, x, dir)
            show(new, y, x, (dir+1) % 4)
            show(new, y, x, (dir+2) % 4)
            go(idx + 1, new)

    elif k == 5:
        new = [now[i][:] for i in range(N)]
        show(new, y, x, 0)
        show(new, y, x, 1)
        show(new, y, x, 2)
        show(new, y, x, 3)
        go(idx + 1, new)


def show(new, y, x, dir):
    global N, M
    ny = y + dy[dir]
    nx = x + dx[dir]
    while 0 <= ny <= N-1 and 0 <= nx <= M-1 and new[ny][nx] != 6:
        if new[ny][nx] == 0:
            new[ny][nx] = 9
        ny += dy[dir]
        nx += dx[dir]
    return


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
cctv = []
for i in range(N):
    for j in range(M):
        if arr[i][j] not in (0, 6):
            cctv.append((i, j, arr[i][j]))

ans = 64
go(0, arr)
print(ans)