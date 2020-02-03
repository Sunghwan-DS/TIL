def numbering(i, j, cnt):
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    queue = [[i, j]]

    while queue:
        lst = queue.pop(0)
        y = lst[0]
        x = lst[1]
        field[y][x] = cnt
        for dir in range(4):
            if 0 <= y+dy[dir] <= N-1 and 0 <= x+dx[dir] <= N-1:
                if field[y+dy[dir]][x+dx[dir]] == 1:
                    queue.append([y+dy[dir], x+dx[dir]])

def BFS(y, x, value):
    global result
    queue = [[y, x]]
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    cnt = 0
    new_field = [[False] * N for i in range(N)]
    new_field[y][x] = True
    while queue:
        for num in range(len(queue)):
            lst = queue.pop(0)
            y = lst[0]
            x = lst[1]
            for dir in range(4):
                if 0 <= y + dy[dir] <= N - 1 and 0 <= x + dx[dir] <= N - 1:
                    new_field[y + dy[dir]][x + dx[dir]] = True
                    if field[y + dy[dir]][x + dx[dir]] == value:
                        pass
                    elif field[y + dy[dir]][x + dx[dir]] == 0:
                        if new_field[y + dy[dir]][x + dx[dir]]:
                            continue
                        else:
                            queue.append([y + dy[dir], x + dx[dir]])
                    elif field[y + dy[dir]][x + dx[dir]] != 0:
                        if cnt < result:
                            result = cnt
                            return
        cnt += 1
        if cnt == result:
            return

N = int(input())
field = []
for _ in range(N):
    field.append(list(map(int,input().split())))

cnt = 1
for i in range(N):
    for j in range(N):
        if field[i][j] == 1:
            cnt += 1
            numbering(i, j, cnt)

result = 200
for i in range(N):
    for j in range(N):
        if field[i][j] != 0:
            BFS(i, j, field[i][j])

print(result)