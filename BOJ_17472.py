# 2020.04.02
# 15:17 ~
#
#

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


def cal_min(start, sequence, res):
    global island_num, ans
    new_sequence = sequence[:]
    new_sequence.append(start)
    if len(new_sequence) == island_num-2:
        print(new_sequence)
        print(res)
        ans = min(ans, res)
        return

    for end in range(2, island_num):
        if bridge_info[start][end]:
            if end not in new_sequence:
                cal_min(end, new_sequence, res + bridge_info[start][end])


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
                    # print(ny, nx, arr[ny][nx], cnt)
                if cnt >= 2:
                    if bridge_info[idx][arr[ny][nx]]:
                        bridge_info[idx][arr[ny][nx]] = min(bridge_info[idx][arr[ny][nx]], cnt)
                        bridge_info[arr[ny][nx]][idx] = bridge_info[idx][arr[ny][nx]]
                    else:
                        bridge_info[idx][arr[ny][nx]] = cnt
                        bridge_info[arr[ny][nx]][idx] = cnt

for i in range(N):
    print(arr[i])
print()

for i in range(island_num):
    print(bridge_info[i])
print()

# for i in range(2, island_num):
#     print(island_edge[i])
# print()

ans = 10000
for start in range(2, island_num):
    cal_min(start, [], 0)

if ans == 10000:
    print(-1)
else:
    print(ans)