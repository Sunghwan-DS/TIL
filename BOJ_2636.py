def air(i, j):
    q = [[i, j]]
    while q:
        current = q.pop(-1)
        y = current[0]
        x = current[1]
        arr[y][x] = 9
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny <= N - 1 and 0 <= nx <= M - 1:
                if arr[ny][nx] == 0:
                    q.append([ny, nx])
                elif arr[ny][nx] == 1:
                    if [ny, nx] not in queue:
                        queue.append([ny, nx])


N, M = map(int,input().split())
arr = []
for i in range(N):
    arr.append(list(map(int,input().split())))

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

queue = []
air(0, 0)

if queue == []:
    print(0)
    print(0)
    exit()

cnt = 0
while queue:
    last = len(queue)
    for _ in range(len(queue)):
        current = queue.pop(0)
        H = current[0]
        W = current[1]
        arr[H][W] = 9
        for d in range(4):
            ny = H + dy[d]
            nx = W + dx[d]
            if 0 <= ny <= N - 1 and 0 <= nx <= M - 1:
                if arr[ny][nx] == 1:
                    if [ny, nx] not in queue:
                        queue.append([ny, nx])
                elif arr[ny][nx] == 0:
                    air(ny, nx)
    cnt += 1

print(cnt)
print(last)