T = int(input())
for case in range(1, T+1):
    N, M, K = map (int,input().split())
    cus = list(map(int,input().split()))
    cus.sort()
    B = 0
    remain = 0
    time = 0
    TF = True
    for t in cus:
        B += (t-time+remain)//M*K
        if B == 0:
            TF = False
            break
        remain = (t - time + remain) % M
        time = t
        B -= 1

    if not TF:
        print("#%d"%(case), "Impossible")
    else:
        print("#%d"%(case), "Possible")