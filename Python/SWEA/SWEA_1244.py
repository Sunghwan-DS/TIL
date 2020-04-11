T = int(input())
for case in range(1, T+1):
    N, K = input().split()
    N = list(N)
    new = N[:].sorted(reverse = True)
    if K == 1:
        if

            N = list(N)
    L = len(N)
    t = 0
    con = 0
    pick = 0
    while K > 0:
        change1 = (N[-1], L-1)
        for i in range(L-2, pick, -1):
            if N[i] > change1[0]:
                change1 = (N[i], i)
        if N[pick] >= change1[0]:
            break
        else:
