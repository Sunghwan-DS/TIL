def DFS(num):
    for i in range(1, N+1):
        if not visited[i] and team[num][i]:
            visited[i] = True
            DFS(i)


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    team = [[False] * (N+1) for _ in range(N+1)]
    visited = [False] * (N+1)

    for idx in range(M):
        A, B = data[idx * 2], data[idx * 2 + 1]
        team[A][B] = True
        team[B][A] = True

    ans = 0
    for num in range(1, N+1):
        if not visited[num]:
            visited[num] = True
            DFS(num)
            ans += 1

    print("#%d"%(tc), ans)