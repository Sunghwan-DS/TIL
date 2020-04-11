def check(lst):
    global N, M, bn, ans
    new = [arr[_][:] for _ in range(N)]
    for wy, wx in lst:
        new[wy][wx] = 1

    res = bn - 3

    for vy, vx in virus:
        s = [(vy, vx)]

        while s:
            y, x = s[-1]
            for dir in range(4):
                ny = y + dy[dir]
                nx = x + dx[dir]

                if 0 <= ny <= N-1 and 0 <= nx <= M-1 and new[ny][nx] == 0:
                    s.append((ny,nx))
                    new[ny][nx] = 2
                    res -= 1
                    break

            else:
                s.pop()

    if ans < res:
        ans = res


N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
virus = []
blank = []
bn = 0
ans = 0

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            virus.append((i, j))
        elif arr[i][j] == 0:
            blank.append((i, j))
            bn += 1

for a in range(bn):
    for b in range(a+1, bn):
        for c in range(b+1, bn):
            check([blank[a], blank[b], blank[c]])


print(ans)