def BFS(p):
    global queue, result
    TF = True
    if p[0] - 1 >= 0 and field[p[0]][p[1]] > field[p[0]-1][p[1]]:
        queue.append([p[0]-1, p[1], p[2]+1])
        TF = False
    if p[0] + 1 <= N-1 and field[p[0]][p[1]] > field[p[0]+1][p[1]]:
        queue.append([p[0]+1, p[1], p[2]+1])
        TF = False
    if p[1] - 1 >= 0 and field[p[0]][p[1]] > field[p[0]][p[1]-1]:
        queue.append([p[0], p[1]-1, p[2]+1])
        TF = False
    if p[1] + 1 <= N-1 and field[p[0]][p[1]] > field[p[0]][p[1]+1]:
        queue.append([p[0], p[1]+1, p[2]+1])
        TF = False
    if TF:
        if result < p[2]:
            result = p[2]

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
                start.append([i, j, 1])

    queue = start

    result = 0

    while queue:
        for i in range(len(queue)):
            current = queue.pop(0)
            BFS(current)
    print("#%d %d"%(case, result))