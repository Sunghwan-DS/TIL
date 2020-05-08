for tc in range(1, int(input()) + 1):
    N = int(input())
    schedule = []
    for _ in range(N):
        s, e = map(int,input().split())
        schedule.append((s, e))
    schedule.sort(key=lambda x: (x[1], -x[0]))

    last_e = 0
    ans = 0
    for s, e in schedule:
        if s >= last_e:
            ans += 1
            last_e = e

    print("#%d"%(tc), ans)