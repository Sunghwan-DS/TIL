def go(idx, visited):
    global N, ans
    if idx == N:
        ans += 1
        return

    for i in range(N):
        if


for tc in range(1, int(input()) + 1):
    N = int(input())
    col_visited = [0] * N

    ans = 0
    for i in range(N):
        col_visited[i] = True
        go(1, col_visited)
        col_visited[i] = False