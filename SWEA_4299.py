T = int(input())
for case in range(1, T+1):
    D, H, M = map(int,input().split())
    ans = 0
    ans += (D - 11) * 1440
    ans += (H - 11) * 60
    ans += (M - 11)

    if ans < 0:
        ans = -1

    print("#%d" % (case), ans)