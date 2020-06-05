def MST():
    cur = 0
    val = [float('inf')] * N
    connected = [False] * N
    val[cur] = 0

    for _ in range(N):
        connected[cur] = True
        min_idx = -1
        min_val = float('inf')

        for nb in range(N):
            if not connected[nb] and distance[cur][nb] < val[nb]:
                val[nb] = distance[cur][nb]

        for idx, v in enumerate(val):
            if not connected[idx] and v < min_val:
                min_val, min_idx = v, idx
        cur = min_idx
    return sum(val)

for tc in range(1, int(input()) + 1):
    N = int(input())
    Xs = list(map(int, input().split()))
    Ys = list(map(int, input().split()))
    E = float(input())
    distance = [[0] * N for _ in range(N)]
    for s in range(N-1):
        for e in range(s + 1, N):
            distance[s][e] = distance[e][s] = abs(Xs[s] - Xs[e]) ** 2 + abs(Ys[s] - Ys[e]) ** 2

    print("#%d"%(tc), round(E * MST()))