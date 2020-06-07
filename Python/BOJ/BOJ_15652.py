def DFS(idx, word):
    if idx == M:
        print(' '.join(list(word)))
        return

    for num in range(1, N+1):
        if word:
            if int(word[len(word) - 1]) <= num:
                DFS(idx + 1, word + str(num))
        else:
            DFS(idx + 1, word + str(num))

N, M = map(int, input().split())
DFS(0, '')