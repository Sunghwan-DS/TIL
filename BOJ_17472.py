# 2020.04.02
# 15:17 ~ 00:24
# 탐색, 백트레킹 구현
# 시간:56ms, 코드 길이:3069B

def issafe (y, x):
    global N, M
    if 0 <= y <= N-1 and 0 <= x <= M-1:
        return True
    else:
        return False


def check_island(i, j, island_num):
    global N, M
    s = [(i, j)]
    arr[i][j] = island_num
    edge = []

    while s:
        y, x = s.pop()
        edge_check = False

        for dirc in range(4):
            ny = y + dy[dirc]
            nx = x + dx[dirc]

            if issafe(ny, nx):
                if arr[ny][nx] == 1:
                    arr[ny][nx] = island_num
                    s.append((ny, nx))
                elif arr[ny][nx] == 0:
                    edge_check = True
        if edge_check:
            edge.append((y, x))

    island_edge.append(edge)


def check(lst):
    global island_num
    road_map = [[0] * island_num for _ in range(island_num)]
    res = 0
    for y, x in lst:
        road_map[y][x] = bridge_info[y][x]
        road_map[x][y] = bridge_info[x][y]
        res += bridge_info[y][x]

    visited = [False] * island_num
    s = [2]
    visited[2] = True
    while s:
        i = s.pop()
        for j in range(2, island_num):
            if road_map[i][j] and not visited[j]:
                s.append(j)
                visited[j] = True
    for i in range(2, island_num):
        if not visited[i]:
            return 10000
    return res


def choose(idx, lst):
    global island_num, roads_num, ans
    if len(lst) == island_num-3:
        ans = min(ans, check(lst))
        return
    if idx == roads_num:
        return

    lst.append(roads[idx])
    choose(idx+1, lst)
    lst.pop()
    choose(idx+1, lst)


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
island_edge = [[],[]]
island_num = 2

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            check_island(i, j, island_num)
            island_num += 1
bridge_info = [[0] * island_num for _ in range(island_num)]

for idx in range(2, island_num):
    for y, x in island_edge[idx]:
        for dirc in range(4):
            ny = y + dy[dirc]
            nx = x + dx[dirc]
            if issafe(ny, nx):
                cnt = 0
                while arr[ny][nx] == 0:
                    cnt += 1
                    ny += dy[dirc]
                    nx += dx[dirc]
                    if not issafe(ny, nx):
                        cnt = 0
                        break
                if cnt >= 2:
                    if bridge_info[idx][arr[ny][nx]]:
                        bridge_info[idx][arr[ny][nx]] = min(bridge_info[idx][arr[ny][nx]], cnt)
                        bridge_info[arr[ny][nx]][idx] = bridge_info[idx][arr[ny][nx]]
                    else:
                        bridge_info[idx][arr[ny][nx]] = cnt
                        bridge_info[arr[ny][nx]][idx] = cnt

roads = []
for i in range(2, island_num):
    for j in range(i+1, island_num):
        if bridge_info[i][j]:
            roads.append((i, j))
roads_num = len(roads)
ans = 10000
choose(0, [])
if ans == 10000:
    print(-1)
else:
    print(ans)