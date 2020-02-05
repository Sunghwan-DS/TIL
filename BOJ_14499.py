def move(dir):
    global y, x
    if dir == 1:
        if x+1 >= M:
            return
        x += 1
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]

    elif dir == 2:
        if x-1 < 0:
            return
        x -= 1
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]

    elif dir == 3:
        if y-1 < 0:
            return
        y -= 1
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]

    elif dir == 4:
        if y+1 >= N:
            return
        y += 1
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]

    if arr[y][x] == 0:
        arr[y][x] = dice[5]
    else:
        dice[5] = arr[y][x]
        arr[y][x] = 0

    return print(dice[0])

N, M, y, x, K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
go = list(map(int,input().split()))
dice = [0, 0, 0, 0, 0, 0]
for _ in range(K):
    move(go[_])