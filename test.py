def BFS(S, G):
    visited = [False] * (V+1)
    visited[S] = True
    q = [S]
    ans = 0
    while q:
        for i in range(len(q)):
            now = q.pop(0)
            if now == G:
                return ans
            for next in range(V + 1):
                if roads[now][next] and not visited[next]:
                    visited[next] = True
                    q.append(next)
        ans += 1
    return 0

for tc in range(1, int(input())+1):
    V, E = map(int,input().split())
    roads = [[False] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        S, G = map(int,input().split())
        roads[S][G] = True
        roads[G][S] = True

    S, G = map(int,input().split())
    print("#%d"%(tc), BFS(S, G))