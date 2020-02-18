def match(low, high):
    if low == high:
        return high

    a = match(low, (low + high) // 2)
    b = match((low + high) // 2 + 1, high)

    if player[a] > player[b]:
        if player[a] == 3 and player[b] == 1:
            return b
        else:
            return a

    elif player[a] == player[b]:
        return min(a, b)

    else:
        if player[a] == 1 and player[b] == 3:
            return a
        else:
            return b


T = int(input())
for case in range(1, T+1):
    N = int(input())
    player = list(map(int,input().split()))
    player.insert(0, 0)
    print("#%d"%(case), match(1, N))