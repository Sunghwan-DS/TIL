for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    connections = [[0] * (V + 1) for _ in range(V + 1)]
    for i in range(E):
        n1, n2, w = map(int, input().split())
        connections[n1][n2] = w
        connections[n2][n1] = w

    INF = float('inf')
    key = [INF] * (V + 1)
    p = [-1] * (V + 1)
    visited = [False] * (V + 1)

    key[0] = 0
    cnt = 0
    ans = 0
    while cnt < V+1:
        min_val = INF
        u = -1
        for i in range(V+1):
            if not visited[i] and key[i] < min_val :
                min_val = key[i]
                u = i
        ans += min_val
        visited[u] = True
        cnt += 1

        for i in range(V+1):
            if 0 < connections[u][i] < key[i] and not visited[i]:
                key[i] = connections[u][i]
                p[i] = u

    print('#%d' % (tc), ans)