def DFS(y, x):
    global R, C
    if len(ans) == R * C - 2 and y == R-1 and x == C-1:
        print(''.join(ans))
        exit()
        return

    for dirc in range(4):
        ny = y + dy[dirc]
        nx = x + dx[dirc]

        if 0 <= ny <= R-1 and 0 <= nx <= C-1 and not visited[ny][nx]:
            visited[ny][nx] = True
            ans.append(direction[dirc])
            DFS(ny, nx)
            visited[ny][nx] = False
            ans.pop()

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
direction = ['D', 'U', 'R', 'L']

R, C = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(R)]

ans = ''
if R%2:
    for idx in range(R):
        if idx%2 == 0:
            ans += 'R' * (C-1)
            ans += 'D'
        else:
            ans += 'L' * (C-1)
            ans += 'D'
    ans = ans[:-1]
    print(ans)

elif C%2:
    for idx in range(C):
        if idx%2 == 0:
            ans += 'D' * (C-1)
            ans += 'R'
        else:
            ans += 'U' * (C-1)
            ans += 'R'
    print(ans)

else:
    min_val = 1000
    min_y = 0
    min_x = 0
    for i in range(R):
        for j in range(C):
            if (i+j) % 2:
                if arr[i][j] < min_val:
                    min_val = arr[i][j]
                    min_y = i
                    min_x = j

    visited = [[False] * C for _ in range(R)]
    visited[min_y][min_x] = True
    visited[0][0] = True
    ans = []
    DFS(0, 0)