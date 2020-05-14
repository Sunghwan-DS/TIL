for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()

    ans = 0
    for num in B:
        l = 0
        r = N - 1
        m = (l + r) // 2
        res = 'A'

        while True:
            if A[m] == num:
                ans += 1
                break
            elif A[m] > num:
                r = m - 1
                m = (l + r) // 2
                if res[-1] == 'l':
                    break
                res += 'l'
            elif A[m] < num:
                l = m + 1
                m = (l + r) // 2
                if res[-1] == 'r':
                    break
                res += 'r'
            if l > r:
                break

    print("#%d"%(tc), ans)