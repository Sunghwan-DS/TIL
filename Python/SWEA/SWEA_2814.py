def go(length, start, new_visited):
    global ans
    for i in range(1, N+1):
        if arr[start][i] and not new_visited[i]:
            new_visited[i] = True
            go(length+1, i, new_visited)
            new_visited[i] = False

    ans = max(ans, length)


for tc in range(1, int(input()) + 1):
    N, M = map(int,input().split())
    arr = [[False] * (N+1) for _ in range(N+1)]
    for i in range(M):
        s, e = map(int,input().split())
        arr[s][e] = True
        arr[e][s] = True

    ans = 0
    visited = [False] * (N + 1)
    for i in range(1, N+1):
        visited[i] = True
        go(1, i, visited)
        visited[i] = False

    print("#%d"%(tc), ans)