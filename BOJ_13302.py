# 2020.02.27
# 11:36 ~ 13:03
# DP 구현
# 시간:68ms, 코드 길이:1038B

N, M = map(int,input().split())
plan = [True] * (N+1)
max_ticket = (N//5)*2 + (N % 5)//3 + 1
state = [[1000000] * max_ticket for _ in range(N+1)]
state[0][0] = 0
if M > 0:
    for i in list(map(int,input().split())):
        plan[i] = False

for day, p in enumerate(plan[1:], 1):
    for i in range(max_ticket):
        if state[day-1][i] < 1000000:
            if p:
                if i >= 3:
                    state[day][i-3] = min(state[day][i-3], state[day-1][i])
                else:
                    state[day][i] = min(state[day-1][i] + 10000, state[day][i])

            else:
                state[day][i] = min(state[day-1][i], state[day][i])

        if day-3 >= 0:
            if state[day-3][i] < 1000000:
                state[day][i+1] = min(state[day-3][i] + 25000, state[day][i+1])

        if day-5 >= 0:
            if state[day-5][i] < 1000000:
                state[day][i+2] = min(state[day-5][i] + 37000, state[day][i+2])

print(min(state[N]))