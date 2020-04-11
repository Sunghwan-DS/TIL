dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
for tc in range(1, int(input())+1):
    R, C = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(R)]
    ans = 0
    fail = [1]
    while fail:
        fail = []
        for i in range(R):
            for j in range(C):
                if arr[i][j]:
                    ans += arr[i][j]
                    neibor = 0
                    neibor_tot = 0
                    for dirc in range(4):
                        ny = i + dy[dirc]
                        nx = j + dx[dirc]
                        if 0 <= ny <= R-1 and 0 <= nx <= C-1:
                            if arr[ny][nx]:
                                neibor += 1
                                neibor_tot += arr[ny][nx]
                            else:
                                ny += dy[dirc]
                                nx += dx[dirc]
                                while 0 <= ny <= R-1 and 0 <= nx <= C-1:
                                    if arr[ny][nx]:
                                        neibor += 1
                                        neibor_tot += arr[ny][nx]
                                        break
                                    ny += dy[dirc]
                                    nx += dx[dirc]
                    if arr[i][j] * neibor < neibor_tot:
                        fail.append((i, j))
        for y, x in fail:
            arr[y][x] = 0
    print("Case #%d:"%(tc), ans)