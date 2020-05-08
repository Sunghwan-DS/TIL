for tc in range(1, int(input()) + 1):
    N, M = map(int,input().split())
    Ws = list(map(int,input().split()))
    Ts = list(map(int,input().split()))
    Ws.sort(reverse=True)
    Ts.sort(reverse=True)
    ans = 0
    idx_w = 0
    for t in Ts:
        while t < Ws[idx_w]:
            idx_w += 1
            if idx_w >= len(Ws):
                break

        if idx_w >= len(Ws):
            break

        ans += Ws[idx_w]
        idx_w += 1

        if idx_w >= len(Ws):
            break

    print("#%d"%(tc), ans)