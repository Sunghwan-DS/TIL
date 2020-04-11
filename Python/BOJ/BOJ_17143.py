def move_shark():
    global arr
    next_arr = [[0] * (C+1) for _ in range(R+1)]
    for s in shark:
        if s[4] == 0:
            continue
        if dy[s[3]] * s[2] < 0:
            ny = s[0] + abs((dy[s[3]] * s[2])) % (2 * R - 2) * (-1)
        else:
            ny = s[0] + (dy[s[3]] * s[2]) % (2*R-2)
        if dx[s[3]] * s[2] < 0:
            nx = s[1] + abs((dx[s[3]] * s[2])) % (2 * C - 2) * (-1)
        else:
            nx = s[1] + (dx[s[3]] * s[2]) % (2*C-2)

        while True:
            if ny > R:
                ny = R - abs(ny - R)
                s[3] = 1
                continue
            elif ny < 1:
                ny = 1 + abs(ny - 1)
                s[3] = 2
                continue
            if nx > C:
                nx = C - abs(nx - C)
                s[3] = 4
            elif nx < 1:
                nx = 1 + abs(nx - 1)
                s[3] = 3
            else:
                break

        if next_arr[ny][nx] > s[4]:
            s[4] = 0
            continue
        elif next_arr[ny][nx] == 0:
            next_arr[ny][nx] = s[4]
            s[0] = ny
            s[1] = nx
        else:
            for eat in shark:
                if eat[4] == next_arr[ny][nx]:
                    eat[4] = 0
                    break
            next_arr[ny][nx] = s[4]
            s[0] = ny
            s[1] = nx
    arr = [next_arr[i][:] for i in range(R + 1)]


R, C, M = map(int,input().split())
arr = [[0] * (C+1) for _ in range(R+1)]

dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, 1, -1]

result = 0
shark = []
for _ in range(M):
    shark.append(list(map(int,input().split())))    # r, c, s, d, z
    arr[shark[_][0]][shark[_][1]] = shark[_][4]

for j in range(1, C+1):
    for i in range(1, R+1):
        if arr[i][j] != 0:
            result += arr[i][j]
            for hunt in shark:
                if hunt[4] == arr[i][j]:
                    hunt[4] = 0
                    break
            arr[i][j] = 0
            break
    move_shark()
print(result)