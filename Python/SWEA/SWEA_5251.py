T = int(input())
for case in range(1, T+1):
    N, E = map(int,input().split())
    price = [[0] * (N + 1) for _ in range(N + 1)]
    min_val = [999999] * (N + 1)
    for t in range(E):
        s, e, w = map(int,input().split())
        price[s][e] = w

    q = [(0,0)]
    min_val[0] = 0
    while q:
        current, p = q.pop(0)
        if p > min_val[current]:
            continue
        for arrive, val in enumerate(price[current]):
            new_val = p + price[current][arrive]
            if val and min_val[arrive] > new_val:
                min_val[arrive] = new_val
                q.append((arrive, new_val))
    print("#%d"%(case), min_val[N])