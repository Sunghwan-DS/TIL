T = int(input())
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
for case in range(1, T+1):
    H, W = map(int,input().split())
    arr = [list(input()) for _ in range(H)]
    input()
    move = input()
    tank = ['^', '<', '>', 'v']

    TF = False
    for H in range(H):
        for W in range(W):
            if arr[H][W] in tank:
                if arr[H][W] == '^':
                    dir = 0
                elif arr[H][W] == '>':
                    dir = 1
                elif arr[H][W] == 'v':
                    dir = 2
                elif arr[H][W] == '<':
                    dir = 3
                arr[H][W] = '.'
                TF = True
                break
        if TF:
            break

    for m in move:
        if m == 'U':
            dir = 0
            ny = H + dy[dir]
            nx = W + dx[dir]
            if 0 <= ny <= H-1 and 0 <= nx <= W-1 and arr[ny][nx] == '.':
                H = ny
                W = nx

        elif m == 'R':
            dir = 1
            ny = H + dy[dir]
            nx = W + dx[dir]
            if 0 <= ny <= H-1 and 0 <= nx <= W-1 and arr[ny][nx] == '.':
                H = ny
                W = nx

        elif m == 'D':
            dir = 2
            ny = H + dy[dir]
            nx = W + dx[dir]
            if 0 <= ny <= H-1 and 0 <= nx <= W-1 and arr[ny][nx] == '.':
                H = ny
                W = nx

        elif m == 'L':
            dir = 3
            ny = H + dy[dir]
            nx = W + dx[dir]
            if 0 <= ny <= H-1 and 0 <= nx <= W-1 and arr[ny][nx] == '.':
                H = ny
                W = nx

        elif m == 'S':
            ny = H + dy[dir]
            nx = W + dx[dir]
            while 0 <= ny <= H-1 and 0 <= nx <= W-1 and arr[ny][nx] not in '*#':
                ny += dy[dir]
                nx += dx[dir]

            if 0 <= ny <= H-1 and 0 <= nx <= W-1:
                if arr[ny][nx] == '#':
                    continue
                else:
                    arr[ny][nx] = '.'

    if dir == 0:
        arr[H][W] = '^'
    elif dir == 1:
        arr[H][W] = '>'
    elif dir == 2:
        arr[H][W] = 'v'
    elif dir == 3:
        arr[H][W] = '<'

    print("#%d"%(case), ''.join(arr[0]))
    for i in range(1, H):
        print(''.join(arr[i]))