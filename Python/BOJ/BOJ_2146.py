def numbering(i, j, cnt):
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    queue = [[i, j]]
    edge_lst = []

    while queue:
        lst = queue.pop(-1)
        y = lst[0]
        x = lst[1]
        field[y][x] = cnt
        for dir in range(4):
            if 0 <= y+dy[dir] <= N-1 and 0 <= x+dx[dir] <= N-1:
                if field[y+dy[dir]][x+dx[dir]] == 1:
                    queue.append([y+dy[dir], x+dx[dir]])
                elif field[y+dy[dir]][x+dx[dir]] == 0:
                    if [y,x] not in edge_lst:
                        edge.append([y,x])


def BFS():
    global result
    queue = edge[:]
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    cnt = 0
    result = 9999

    while queue:
        for num in range(len(queue)):
            lst = queue.pop(0)
            y = lst[0]
            x = lst[1]
            value = field[y][x]
            for dir in range(4):
                if 0 <= y + dy[dir] <= N - 1 and 0 <= x + dx[dir] <= N - 1:
                    if field[y + dy[dir]][x + dx[dir]] == value:
                        pass
                    elif field[y + dy[dir]][x + dx[dir]] == 0:
                        field[y + dy[dir]][x + dx[dir]] = value
                        queue.append([y + dy[dir], x + dx[dir]])
                    elif field[y + dy[dir]][x + dx[dir]] != 0:
                        if field[y + dy[dir]][x + dx[dir]] > value:
                            if result > cnt*2:
                                result = cnt*2
                        else:
                            if result > cnt*2+1:
                                result = cnt*2+1
        if result != 9999:
            return result
        cnt += 1

N = int(input())
field = []
for _ in range(N):
    field.append(list(map(int,input().split())))
edge = []
cnt = 1
for i in range(N):
    for j in range(N):
        if field[i][j] == 1:
            cnt += 1
            numbering(i, j, cnt)


print(BFS())