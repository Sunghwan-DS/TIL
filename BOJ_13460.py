def move(y_R, x_R, y_B, x_B, dir, idx):
    global result
    if idx == 11:
        return

    if idx == result:
        return

    for _ in range(2):
        while arr[y_R + dy[dir]][x_R + dx[dir]] == '.':
            y_R += dy[dir]
            x_R += dx[dir]

        if arr[y_R + dy[dir]][x_R + dx[dir]] == 'O':
            if idx + 1 < result:
                result = idx + 1
            return


        while arr[y_B + dy[dir]][x_B + dx[dir]] == '.':
            y_R += dy[dir]
            x_R += dx[dir]

        if arr[y_B + dy[dir]][x_B + dx[dir]] == 'O':
            return

    for i in range(4):
        move(y_R, x_R, y_B, x_B, i, idx + 1)

N, M = map(int,input().split())
arr = [input() for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# print(arr)

for i in range(N):
    for j in range(M):
        if arr[i][j] == "R":
            y_R = i
            x_R = j
        if arr[i][j] == "B":
            y_B = i
            x_B = j

list(map(int,list(input())))

result = 20

for i in range(4):
    move(y_R, x_R, y_B, x_B, i, 0)

if result > 10:
    print(-1)
else:
    print(result)
