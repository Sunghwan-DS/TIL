def DFS(idx, res):
    global ans, N
    if idx == N:
        ans = min(ans, res)
        return

    if res >= ans:
        return

    for num in range(N):
        if not visited[num]:
            visited[num] = True
            DFS(idx+1, res + arr[idx][num])
            visited[num] = False


for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N
    ans = 99 * 15
    DFS(0, 0)
    print("#%d"%(tc), ans)