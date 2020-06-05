def make(idx, lst):
    global ans
    res = sum(lst) - B
    if res > ans:
        return
    elif res >= 0:
        ans = min(ans, res)

    if idx == N:
        return

    lst.append(H[idx])
    make(idx + 1, lst)
    lst.pop()
    make(idx + 1, lst)


for tc in range(1, int(input()) + 1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    ans = 1000000
    make(0, [])
    print("#%d"%(tc), ans)