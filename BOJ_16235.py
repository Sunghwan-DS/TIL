def go():
    die = []
    for t in tree:
        z = t[0]
        y = t[1]
        x = t[2]

        if arr[y][x] - z >= 0:
            arr[y][x] -= z
            t[0] += 1
        else:
            die.append(t)

    for di in die:
        tree.remove(di)
        z = di[0]
        y = di[1]
        x = di[2]
        arr[y][x] += (z//2)

    new = []
    for t in tree:
        z = t[0]
        if z % 5 == 0:
            y = t[1]
            x = t[2]

            for dir in range(8):
                ny = y + dy[dir]
                nx = x + dx[dir]

                if 0 <= ny <= N-1 and 0 <= nx <= N-1:
                    new.append([1, ny, nx])

    for a in new:
        tree.insert(0, a)

    for i in range(N):
        for j in range(N):
            arr[i][j] += feed[i][j]


N, M, K = map(int,input().split())
feed = [list(map(int,input().split())) for _ in range(N)]
arr = [[5] * N for _ in range(N)]
tree = []

dy = [1, 1, 1, 0, 0, -1, -1, -1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]

for _ in range(M):
    x, y, z = map(int,input().split())
    tree.append([z, y-1, x-1])
tree.sort()

for year in range(K):
    go()

print(len(tree))