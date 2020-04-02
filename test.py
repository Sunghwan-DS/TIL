for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    pizzas = list(map(int, input().split()))
    index = 1
    oven = []
    for i in range(N):
        pizza = pizzas.pop(0)
        oven.append([pizza, index])
        index += 1

    idx = 0
    while oven:
        if oven[idx][0] == 0:
            zero, ans = oven.pop(idx)
            N -= 1
            if N == 0:
                break
            else:
                idx %= N
                continue

        oven[idx][0] //= 2
        if oven[idx][0] == 0:
            if pizzas:
                oven[idx] = [pizzas.pop(0), index]
                index += 1
        idx = (idx+1) % N

    print("#%d" % (tc), ans)