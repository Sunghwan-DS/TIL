def DFS(y, x, k, cnt):
    global result
    print(cnt,y, x)
    if y - 1 >= 0:
        if field[y][x] > field[y-1][x]:
            DFS(y-1, x, k, cnt+1)
        elif field[y][x] > field[y-1][x] - k:
            pre = field[y-1][x]
            field[y-1][x] = field[y][x] - 1
            DFS(y-1, x, 0, cnt+1)
            field[y-1][x] = pre

    if y + 1 <= N-1:
        if field[y][x] > field[y+1][x]:
            DFS(y+1, x, k, cnt+1)
        elif field[y][x] > field[y+1][x] - k:
            pre = field[y+1][x]
            field[y+1][x] = field[y][x] - 1
            DFS(y+1, x, 0, cnt+1)
            field[y+1][x] = pre

    if x - 1 >= 0:
        if field[y][x] > field[y][x-1]:
            DFS(y, x-1, k, cnt+1)
        elif field[y][x] > field[y][x-1] - k:
            pre = field[y][x-1]
            field[y][x-1] = field[y][x] - 1
            DFS(y, x-1, 0, cnt+1)
            field[y][x-1] = pre

    if x + 1 <= N-1:
        if field[y][x] > field[y][x+1]:
            DFS(y, x+1, k, cnt+1)
        elif field[y][x] > field[y][x+1] - k:
            pre = field[y][x+1]
            field[y][x+1] = field[y][x] - 1
            DFS(y, x+1, 0, cnt+1)
            field[y][x+1] = pre

    if result < cnt:
        result = cnt

T = int(input())
for case in range(1, T+1):
    N, K = map(int,input().split())
    field = []
    check_max = []
    start = []
    for _ in range(N):
        field.append(list(map(int,input().split())))
        check_max.append(max(field[_]))

    max_num = max(check_max)

    for i in range(N):
        for j in range(N):
            if field[i][j] == max_num:
                start.append([i, j])

    result = 0

    for i in start:
        DFS(i[0], i[1], K, 1)
    print("#%d %d"%(case, result))