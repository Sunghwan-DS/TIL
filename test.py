for case in range(1, 11):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    ans = 0
    for j in range(N):
        i = 0
        cnt = 0
        while i < N:
            if arr[i][j] == 1:
                cnt += 1
                s = 1
                break
            i += 1

        i += 1
        while i < N:
            if arr[i][j] != 0 and arr[i][j] != s:
                cnt += 1
                s = arr[i][j]
            i += 1

        ans += cnt//2

    print("#%d"%(case), ans)