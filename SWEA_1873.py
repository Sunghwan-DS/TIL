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
    for y in range(H):
        for x in range(W):
            if arr[y][x] in tank:
                if arr[y][x] == '^':
                    dir = 0
                elif arr[y][x] == '>':
                    dir = 1
                elif arr[y][x] == 'v':
                    dir = 2
                elif arr[y][x] == '<':
                    dir = 3
                arr[y][x] = '.'
                TF = True
                break
        if TF:
            break

    for m in move:
        if m == 'U':
            dir = 0
            ny = y + dy[dir]
            nx = x + dx[dir]
            if 0 <= ny <= H-1 and 0 <= nx <= W-1 and arr[ny][nx] == '.':
                y = ny
                x = nx

        elif m == 'R':
            dir = 1
            ny = y + dy[dir]
            nx = x + dx[dir]
            if 0 <= ny <= H-1 and 0 <= nx <= W-1 and arr[ny][nx] == '.':
                y = ny
                x = nx

        elif m == 'D':
            dir = 2
            ny = y + dy[dir]
            nx = x + dx[dir]
            if 0 <= ny <= H-1 and 0 <= nx <= W-1 and arr[ny][nx] == '.':
                y = ny
                x = nx

        elif m == 'L':
            dir = 3
            ny = y + dy[dir]
            nx = x + dx[dir]
            if 0 <= ny <= H-1 and 0 <= nx <= W-1 and arr[ny][nx] == '.':
                y = ny
                x = nx

        elif m == 'S':
            ny = y + dy[dir]
            nx = x + dx[dir]
            while 0 <= ny <= H-1 and 0 <= nx <= W-1 and arr[ny][nx] not in '*#':
                ny += dy[dir]
                nx += dx[dir]

            if 0 <= ny <= H-1 and 0 <= nx <= W-1:
                if arr[ny][nx] == '#':
                    continue
                else:
                    arr[ny][nx] = '.'

    if dir == 0:
        arr[y][x] ='^'
    elif dir == 1:
        arr[y][x] = '>'
    elif dir == 2:
        arr[y][x] = 'v'
    elif dir == 3:
        arr[y][x] = '<'

    print("#%d"%(case), ''.join(arr[0]))
    for i in range(1, H):
        print(''.join(arr[i]))