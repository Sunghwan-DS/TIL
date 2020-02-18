T = int(input())
for case in range(1, T+1):
    data = input()
    ans = 0
    res = 0
    for idx, i in enumerate(data):
        i = int(i)
        if idx <= res:
            res += i
        else:
            k = idx - res
            ans += k
            res += k
            res += i

    print("#%d"%(case), ans)