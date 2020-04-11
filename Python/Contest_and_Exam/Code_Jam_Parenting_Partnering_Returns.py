for T in range(1, int(input()) + 1):
    N = int(input())
    schedule = []
    ans = [0] * N
    for i in range(N):
        S, E = map(int,input().split())
        schedule.append((S, E, i))
    schedule.sort()
    C_end, J_end = 0, 0
    for S, E, i in schedule:
        if S >= C_end:
            ans[i] = 'C'
            C_end = E
        elif S >= J_end:
            ans[i] = 'J'
            J_end = E
        else:
            ans = 'IMPOSSIBLE'
            break
    print("Case #%d:"%(T), ''.join(ans))