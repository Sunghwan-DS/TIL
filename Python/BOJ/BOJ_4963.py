def zero(y, x):
    queue=[[y, x]]
    while queue:
        a = queue.pop(-1)
        y = a[0]
        x = a[1]
        field[y][x] = 0
        for d in range(8):
            if 0 <= y+dy[d] <= H-1 and 0 <= x+dx[d] <= w-1:
                if field[y+dy[d]][x+dx[d]] == 1:
                    queue.append([y+dy[d], x+dx[d]])


dy = [0, 0, 1, 1, 1, -1, -1, -1]
dx = [-1, 1, -1, 0, 1, -1, 0, 1]

while True:
    w, H = map(int, input().split())
    if w == 0:
        exit()
    cnt = 0
    field = []
    for i in range(H):
        field.append(list(map(int,input().split())))

    for i in range(H):
        for j in range(w):
            if field[i][j] == 1:
                zero(i, j)
                cnt += 1
    print(cnt)