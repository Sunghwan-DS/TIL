for tc in range(1, int(input()) + 1):
    N = int(input())
    ans = [0] * 200
    for _ in range(N):
        s, e = map(int,input().split())
        for i in range(min(s-1, e-1)//2, max(s-1, e-1)//2 + 1):
            ans[i] += 1

    print("#%d"%(tc), max(ans))