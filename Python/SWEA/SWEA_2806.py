def go(idx):
    global N, ans
    if idx == N:
        ans += 1
        return

    for i in range(N):
        if not row_visited[i]:
            for j in range(idx):
                if idx - j == abs(i - col[j]):
                    break

            else:
                row_visited[i] = True
                col[idx] = i
                go(idx+1)
                row_visited[i] = False
                col[idx] = 0


for tc in range(1, int(input()) + 1):
    N = int(input())
    row_visited = [False] * N
    col = [0] * N

    ans = 0
    for i in range(N):
        row_visited[i] = True
        col[0] = i
        go(1)
        row_visited[i] = False
        col[0] = 0

    print("#%d"%(tc), ans)