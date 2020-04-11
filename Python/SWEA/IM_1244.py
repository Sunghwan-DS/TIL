def change(state):
    if state == 0:
        return 1
    elif state == 1:
        return 0

N = int(input())
bulb = list(map(int, input().split()))
student = int(input())
for _ in range(student):
    s, card = map(int, input().split())
    if s == 1:
        for index in range(N):
            if (index+1) % card == 0:
                bulb[index] = change(bulb[index])

    elif s == 2:
        max_range = min(card-1, N-card)
        bulb[card-1] = change(bulb[card-1])
        for check in range(1, max_range+1):
            if bulb[card - 1 -check] == bulb[card - 1 + check]:
                bulb[card - 1 - check] = change(bulb[card - 1 - check])
                bulb[card - 1 + check] = change(bulb[card - 1 + check])
            else:
                break

T = N // 20
for i in range(T):
    print(" ".join([str(i) for i in bulb[i*20:(i+1)*20]]))
print(" ".join([str(i) for i in bulb[T*20:]]))