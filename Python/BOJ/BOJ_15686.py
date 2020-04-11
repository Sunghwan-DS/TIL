def BFS(ch):
    global result
    lst = [200] * len(house)
    for i in range(len(house)):
        for j in range(len(ch)):
            value = abs(house[i][0] - ch[j][0]) + abs(house[i][1] - ch[j][1])
            if value < lst[i]:
                lst[i] = value

    result.append(sum(lst))
    return


def select_chicken(lst, idx):
    global M
    if len(lst) == M:
        BFS(lst)
        return

    elif len(lst) + len(chicken_init) - idx < M:
        return

    select_chicken(lst, idx + 1)
    lst.append(chicken_init[idx])
    select_chicken(lst, idx+1)
    lst.pop(-1)


N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]
result = []

chicken_init = []
house = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            chicken_init.append([i, j])
        elif arr[i][j] == 1:
            house.append([i, j])
select_chicken([], 0)

print(min(result))