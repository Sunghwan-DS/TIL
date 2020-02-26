# 2020.02.26
# 16:59 ~
#
#

N, M = map(int,input().split())
plan = [True] * (N+1)
state = [(0, 0)] * (N+1)
if M > 0:
    for i in list(map(int,input().split())):
        plan[i] = False

for day, p in enumerate(plan[1:], 1):
    if p:
        if state[day-1][1] >= 3:
            p1 = (state[day-1][0], state[day-1][1]-3)
        else:
            p1 = (state[day-1][0] + 10000, state[day-1][1])

        if day-3 >= 0:
            p2 = (state[day-3][0] + 25000, state[day-3][1] + 1)
        else:
            p2 = (100000, 0)

        if day-5 >= 0:
            p3 = (state[day-5][0] + 37000, state[day-5][1] + 2)
        else:
            p3 = (100000, 0)

        state[day] = min(p1, p2, p3)
    else:
        state[day] = state[day-1]

print(state[-1][0])
print(state)