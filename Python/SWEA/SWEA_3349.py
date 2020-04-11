for tc in range(1, int(input()) + 1):
    W, H, N = map(int,input().split())
    x, y = map(int,input().split())

    ans = 0
    for _ in range(N-1):
        nx, ny = map(int,input().split())
        dx = nx - x
        dy = ny - y
        if dx * dy >= 0:
            ans += max(abs(dx), abs(dy))
        else:
            ans += abs(dx) + abs(dy)
        x, y = nx, ny

    print("#%d"%(tc), ans)