def check_size(y, x):
    ny = y
    nx = x

    while ny <= N-1 and arr[ny][nx] != 0:
        ny += 1
    ny -= 1

    while nx <= N-1 and arr[ny][nx] != 0:
        nx += 1
    nx -= 1

    dy = ny - y + 1
    dx = nx - x + 1
    res.append((dy*dx, dy, dx))

    for i in range(y, ny+1):
        for j in range(x, nx+1):
            arr[i][j] = 0
    return


T = int(input())
for case in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    res = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                check_size(i, j)

    res.sort()
    ans = []
    for A, i, j in res:
        ans.append(i)
        ans.append(j)

    print("#%d %d"%(case, len(res)), *ans)