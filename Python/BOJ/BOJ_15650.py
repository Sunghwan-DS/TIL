def DFS(idx, word):
    if idx == M:
        print(' '.join(list(word)))
        return

    for num in range(1, N+1):
        if not visited[num]:
            if not word or num > int(word[-1]):
                visited[num] = True
                DFS(idx + 1, word + str(num))
                visited[num] = False

N, M = map(int, input().split())
visited = [False] * (N + 1)
DFS(0, '')