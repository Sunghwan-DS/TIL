N = int(input())
for tc in range(1, N+1):
    f = float(input())
    ans = ''
    val = 0
    cnt = 1
    while val != f and cnt <= 13:
        if val + 0.5 ** cnt <= f:
            ans += '1'
            val += 0.5 ** cnt
        else:
            ans += '0'
        cnt += 1
    if cnt > 13:
        print("#%d"%(tc), 'overflow')
    else:
        print("#%d"%(tc), ans)