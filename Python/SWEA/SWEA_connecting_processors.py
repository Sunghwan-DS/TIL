def dir_lst(idx, lst):
    global max_n
    if idx == len(cores):
        if max_n == len(cores) and 4 in lst:
            return
        go(lst)
        return

    for dir in cores[idx][2]:
        lst.append(dir)
        dir_lst(idx+1, lst)
        lst.pop()


def go(lst):
    global N, max_n, ans
    visited = [[False] * N for _ in range(N)]
    res_n = 0
    res_l = 0
    for idx, dir in enumerate(lst):
        if res_n + (len(cores) - idx) < max_n:
            return

        if dir == 4:
            continue

        else:
            y = cores[idx][0]
            x = cores[idx][1]
            ny = y + dy[dir]
            nx = x + dx[dir]
            while 0 <= ny <= N-1 and 0 <= nx <= N-1:
                if not visited[ny][nx] and arr[ny][nx] == 0:
                    visited[ny][nx] = True
                    res_l += 1
                    if res_n + (len(cores) - idx) == max_n and ans <= res_l:
                        return
                    ny += dy[dir]
                    nx += dx[dir]

                else:
                    return

            res_n += 1

    if res_n > max_n:
        max_n = res_n
        ans = res_l

    elif res_n == max_n:
        ans = min(ans, res_l)


T = int(input())
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for case in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    check = [[[] for __ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                check[i][j].append(3)
                break

    for j in range(N):
        for i in range(N):
            if arr[i][j] == 1:
                check[i][j].append(0)
                break

    for i in range(N):
        for j in range(N-1, -1, -1):
            if arr[i][j] == 1:
                check[i][j].append(1)
                break

    for j in range(N):
        for i in range(N-1, -1, -1):
            if arr[i][j] == 1:
                check[i][j].append(2)
                break

    cores = []
    ans = 0
    for i in range(1, N-1):
        for j in range(1, N-1):
            if check[i][j]:
                check[i][j].append(4)
                cores.append((i, j, check[i][j]))
    max_n = 0
    dir_lst(0, [])

    print("#%d"%(case), ans)