def go():
    global tree
    die = []
    new = []
    for idx, t in enumerate(tree):
        z = t[0]
        y = t[1]
        x = t[2]

        if arr[y][x] - z >= 0:
            arr[y][x] -= z
            t[0] += 1
            if t[0] % 5 == 0:
                for dir in range(8):
                    ny = y + dy[dir]
                    nx = x + dx[dir]

                    if 0 <= ny <= N-1 and 0 <= nx <= N-1:
                        new.append([1, ny, nx])
        else:
            die.append(idx)

    for idx in die[::-1]:
        d = tree.pop(idx)
        z = d[0]
        y = d[1]
        x = d[2]
        arr[y][x] += (z//2)

    tree = new + tree

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
    y, x, z = map(int,input().split())
    tree.append([z, y-1, x-1])
tree.sort()

for year in range(K):
    go()

print(len(tree))