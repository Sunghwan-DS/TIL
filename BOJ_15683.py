def camera(lst, arr):
    global result, M
    for idx, dir in enumerate(lst):
        if arr[cctv[idx][0]][cctv[idx][1]] == 1:
            y = cctv[idx][0]
            x = cctv[idx][1]
            ny = y + dy[dir]
            nx = x + dx[dir]
            while 0 <= ny <= N-1 and 0 <= nx <= M-1 and arr[ny][nx] != 6:
                if arr[ny][nx] == 0:
                    arr[ny][nx] = 7
                ny += dy[dir]
                nx += dx[dir]

        elif arr[cctv[idx][0]][cctv[idx][1]] == 2:
            y = cctv[idx][0]
            x = cctv[idx][1]
            ny1 = y + dy[dir]
            nx1 = x + dx[dir]
            ny2 = y + dy[(dir+2)%4]
            nx2 = x + dx[(dir+2)%4]
            while 0 <= ny1 <= N-1 and 0 <= nx1 <= M-1 and arr[ny1][nx1] != 6:
                if arr[ny1][nx1] == 0:
                    arr[ny1][nx1] = 7
                ny1 += dy[dir]
                nx1 += dx[dir]

            while 0 <= ny2 <= N-1 and 0 <= nx2 <= M-1 and arr[ny2][nx2] != 6:
                if arr[ny2][nx2] == 0:
                    arr[ny2][nx2] = 7
                ny2 += dy[(dir+2)%4]
                nx2 += dx[(dir+2)%4]

        elif arr[cctv[idx][0]][cctv[idx][1]] == 3:
            y = cctv[idx][0]
            x = cctv[idx][1]
            ny1 = y + dy[dir]
            nx1 = x + dx[dir]
            ny2 = y + dy[(dir + 1) % 4]
            nx2 = x + dx[(dir + 1) % 4]
            while 0 <= ny1 <= N-1 and 0 <= nx1 <= M-1 and arr[ny1][nx1] != 6:
                if arr[ny1][nx1] == 0:
                    arr[ny1][nx1] = 7
                ny1 += dy[dir]
                nx1 += dx[dir]

            while 0 <= ny2 <= N-1 and 0 <= nx2 <= M-1 and arr[ny2][nx2] != 6:
                if arr[ny2][nx2] == 0:
                    arr[ny2][nx2] = 7
                ny2 += dy[(dir + 1) % 4]
                nx2 += dx[(dir + 1) % 4]

        elif arr[cctv[idx][0]][cctv[idx][1]] == 4:
            y = cctv[idx][0]
            x = cctv[idx][1]
            ny1 = y + dy[dir]
            nx1 = x + dx[dir]
            ny2 = y + dy[(dir + 1) % 4]
            nx2 = x + dx[(dir + 1) % 4]
            ny3 = y + dy[(dir + 2) % 4]
            nx3 = x + dx[(dir + 2) % 4]

            while 0 <= ny1 <= N-1 and 0 <= nx1 <= M-1 and arr[ny1][nx1] != 6:
                if arr[ny1][nx1] == 0:
                    arr[ny1][nx1] = 7
                ny1 += dy[dir]
                nx1 += dx[dir]

            while 0 <= ny2 <= N-1 and 0 <= nx2 <= M-1 and arr[ny2][nx2] != 6:
                if arr[ny2][nx2] == 0:
                    arr[ny2][nx2] = 7
                ny2 += dy[(dir + 1) % 4]
                nx2 += dx[(dir + 1) % 4]

            while 0 <= ny3 <= N-1 and 0 <= nx3 <= M-1 and arr[ny3][nx3] != 6:
                if arr[ny3][nx3] == 0:
                    arr[ny3][nx3] = 7
                ny3 += dy[(dir + 2) % 4]
                nx3 += dx[(dir + 2) % 4]

        elif arr[cctv[idx][0]][cctv[idx][1]] == 5:
            y = cctv[idx][0]
            x = cctv[idx][1]
            ny1 = y + dy[dir]
            nx1 = x + dx[dir]
            ny2 = y + dy[(dir + 1) % 4]
            nx2 = x + dx[(dir + 1) % 4]
            ny3 = y + dy[(dir + 2) % 4]
            nx3 = x + dx[(dir + 2) % 4]
            ny4 = y + dy[(dir + 3) % 4]
            nx4 = x + dx[(dir + 3) % 4]

            while 0 <= ny1 <= N-1 and 0 <= nx1 <= M-1 and arr[ny1][nx1] != 6:
                if arr[ny1][nx1] == 0:
                    arr[ny1][nx1] = 7
                ny1 += dy[dir]
                nx1 += dx[dir]

            while 0 <= ny2 <= N-1 and 0 <= nx2 <= M-1 and arr[ny2][nx2] != 6:
                if arr[ny2][nx2] == 0:
                    arr[ny2][nx2] = 7
                ny2 += dy[(dir + 1) % 4]
                nx2 += dx[(dir + 1) % 4]

            while 0 <= ny3 <= N-1 and 0 <= nx3 <= M-1 and arr[ny3][nx3] != 6:
                if arr[ny3][nx3] == 0:
                    arr[ny3][nx3] = 7
                ny3 += dy[(dir + 2) % 4]
                nx3 += dx[(dir + 2) % 4]

            while 0 <= ny4 <= N-1 and 0 <= nx4 <= M-1 and arr[ny4][nx4] != 6:
                if arr[ny4][nx4] == 0:
                    arr[ny4][nx4] = 7
                ny4 += dy[(dir + 3) % 4]
                nx4 += dx[(dir + 3) % 4]

    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                cnt += 1

    if result > cnt:
        result = cnt
    return


def make(idx, lst):
    global n, N
    if idx == n:
        new_arr = [i[:] for i in arr_init]
        camera(lst, new_arr)

        return

    for num in range(4):
        lst.append(num)
        make(idx+1, lst)
        lst.pop(-1)


N, M = map(int,input().split())
arr_init = [list(map(int,input().split())) for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
dir = [0, 1, 2, 3]
result = N * M

cctv = []
for i in range(N):
    for j in range(M):
        if arr_init[i][j] not in [0, 6]:
            cctv.append([i, j, arr_init[i][j]])

n = len(cctv)

make(0, [])

print(result)