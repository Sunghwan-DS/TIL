import itertools

def go(j):
    for i in range(H):
        if new[i][j] != 0:
            bomb(i, j)
            break


def bomb(y, x):
    global H, W
    val = new[y][x]
    new[y][x] = 0

    for len in range(1, val):
        for dir in range(4):
            ny = y + len * dy[dir]
            nx = x + len * dx[dir]

            if 0 <= ny <= H-1 and 0 <= nx <= W-1 and new[ny][nx] != 0:
                bomb(ny, nx)


def gravity():
    for j in range(W):
        i = H-1
        while new[i][j] != 0 and i >= 0:
            i -= 1

        save = i
        i -= 1

        while i >= 0:
            if new[i][j] != 0:
                new[save][j] = new[i][j]
                new[i][j] = 0
                save -= 1
            i -= 1

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

T = int(input())
for case in range(1, T+1):
    N, W, H = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(H)]
    lst = list(itertools.product([i for i in range(W)], repeat = N))
    ans = 180

    for a in lst:
        new = [arr[_][:] for _ in range(H)]

        for b in a:
            go(b)
            gravity()

        res = 0
        for i in range(H):
            for j in range(W):
                if new[i][j] != 0:
                    res += 1

        ans = min(ans, res)

        if ans == 0:
            break

    print("#%d"%(case), ans)