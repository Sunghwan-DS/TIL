T = int(input())
for case in range(1, T+1):
    prices = list(map(int,input().split()))
    plan = list(map(int,input().split()))

    res = [0] + [3000] * 12

    for month, use in enumerate(plan, 1):
        if use:
            res[month] = min(res[month], res[month - 1] + use * prices[0], res[month-1] + prices[1])
        else:
            res[month] = min(res[month-1], res[month])

        if month-3 >= 0:
            res[month] = min(res[month], res[month-3] + prices[2], prices[3])

    print("#%d"%(case), res[-1])