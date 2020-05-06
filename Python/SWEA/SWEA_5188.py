for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    DP = [[0] * N for _ in range(N)]
    sum_y = 0
    for i in range(N):
        sum_y += arr[i][0]
        DP[i][0] = sum_y

    sum_x = 0
    for j in range(N):
        sum_x += arr[0][j]
        DP[0][j] = sum_x

    for i in range(1, N):
        for j in range(1, N):
            DP[i][j] = min(DP[i-1][j], DP[i][j-1]) + arr[i][j]

    print("#%d"%(tc), DP[N-1][N-1])