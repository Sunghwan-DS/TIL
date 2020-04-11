for tc in range(1, int(input()) + 1):
    N, M = map(int,input().split())

    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    ans = 0
    max_times = 0
    for num, i in enumerate(A, 1):
        times = 0
        for idx, j in enumerate(B):
            if i <= j:
                times += 1
                B[idx] = 0
        if max_times < times:
            ans = num
            max_times = times

    print("#%d"%(tc), ans)