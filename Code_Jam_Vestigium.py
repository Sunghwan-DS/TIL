for T in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    k, r, c = 0, 0, 0

    for i in range(N):
        k += arr[i][i]

    for i in range(N):
        a = set(arr[i])
        if len(set(a)) != N:
            r += 1

    new_arr = list(map(list, zip(*arr)))
    for i in range(N):
        a = set(new_arr[i])
        if len(set(a)) != N:
            c += 1

    print("Case #%d:" % (T), k, r, c)