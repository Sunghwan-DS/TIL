def go(start):
    global result
    queue = [start[:]]
    field[start[0]][start[1]] = 0
    cnt = 1
    while queue:
        coordinates = queue.pop(0)
        y = coordinates[0]
        x = coordinates[1]
        field[y][x] = 0
        if y - 1 >= 0:
            if field[y-1][x] == 1:
                field[y-1][x] = 0
                queue.append([y-1, x])
                cnt += 1
        if x - 1 >= 0:
            if field[y][x-1] == 1:
                field[y][x-1] = 0
                queue.append([y, x-1])
                cnt += 1
        if y + 1 <= N-1:
            if field[y+1][x] == 1:
                field[y+1][x] = 0
                queue.append([y+1, x])
                cnt += 1
        if x + 1 <= N-1:
            if field[y][x+1] == 1:
                field[y][x+1] = 0
                queue.append([y, x+1])
                cnt += 1
    result.append(cnt)


N = int(input())
result = []
field = []
for _ in range(N):
    field.append(list(map(int,list(input()))))

for i in range(N):
    for j in range(N):
        if field[i][j] == 1:
            go([i,j])
result.sort()
print(len(result))
for i in result:
    print(i)