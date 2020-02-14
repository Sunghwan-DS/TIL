def make_block(idx, y, x, visited):
    global ans
    new = visited[:]
    new.append([y, x])
    if idx == 3:
        result = 0
        for co in new:
            result += arr[co[0]][co[1]]

        if ans < result:
            ans = result
        return

    lst = []
    for dir in range(3):
        ny = y + dy[dir]
        nx = x + dx[dir]

        if 0 <= ny <= N - 1 and 0 <= nx <= M - 1 and [ny, nx] not in new:
            make_block(idx+1, ny, nx, new)
            lst.append(arr[ny][nx])

    if idx == 0:
        if 0 <= y-1:
            lst.append(arr[y-1][x])

        if len(lst) == 4:
            result = sum(lst) - min(lst) + arr[y][x]
            if ans < result:
                ans = result

        elif len(lst) == 3:
            result = sum(lst) + arr[y][x]
            if ans < result:
                ans = result


N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

dy = [0, 1, 0]
dx = [1, 0, -1]
ans = 0
for i in range(N):
    for j in range(M):
        make_block(0, i, j, [])

print(ans)