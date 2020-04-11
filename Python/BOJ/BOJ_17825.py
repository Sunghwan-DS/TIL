# 2020.04.03
# 10:38 ~ 12:28
# 시뮬레이션 구현
# 시간:132ms, 코드 길이:1412B

def game(idx, horses, score):
    global ans
    check_set = set()
    start_end = 0
    for i in range(4):
        location = table[horses[i][0]][horses[i][1]]
        if location == 0 or location == 1000:
            start_end += 1
        else:
            check_set.add(location)
    if len(check_set) + start_end < 4:
        return

    if idx == 10:
        ans = max(ans, score%1000)
        return

    for i in range(4):
        if i > 0 and horses[i-1][1] == 0:
            continue
        if table[horses[i][0]][horses[i][1]] == 1000:
            continue
        prev = (horses[i][0], horses[i][1])
        horses[i][1] += dice[idx]
        if table[horses[i][0]][horses[i][1]] == 10:
            horses[i][0] = 1
        elif table[horses[i][0]][horses[i][1]] == 20:
            horses[i][0] = 2
        elif table[horses[i][0]][horses[i][1]] == 30:
            horses[i][0] = 3
        game(idx+1, horses, score + table[horses[i][0]][horses[i][1]])
        horses[i][0], horses[i][1] = prev


dice = list(map(int,input().split()))
table = []
table.append([i for i in range(0, 41, 2)] + [1000] * 5)
table.append([0] * 5 + [10, 13, 1016, 19, 25, 1030, 35, 40] + [1000] * 5)
table.append([0] * 10 + [20, 1022, 1024, 25, 1030, 35, 40] + [1000] * 5)
table.append([0] * 15 + [30, 1028, 27, 1026, 25, 1030, 35, 40] + [1000] * 5)

horses = [[0, 0] for _ in range(4)]
ans = 0
game(0, horses, 0)
print(ans)