T = int(input())
for case in range(1, T+1):
    N = int(input())
    price = list(map(int,input().split()))
    sell = price[-1]
    result = 0
    for idx in range(N-2, -1, -1):
        if price[idx] < sell:
            result += (sell - price[idx])
        else:
            sell = price[idx]

    print("#%d %d"%(case, result))