# 2020.03.21
# 14:41 ~ 15:32
#
#


def BFS(new_Gq, new_Rq):
    global N, M, ans
    Gq = new_Gq[:]
    Rq = new_Rq[:]
    visited = [[2500] * M for _ in range(N)]

    for y, x in Gq:
        visited[y][x] = 0
    for y, x in Rq:
        visited[y][x] = 0

    cnt = 1
    res = 0
    while Gq and Rq:
        n_Gq = set()
        n_Rq = set()
        for i in range(len(Gq)):
            y, x = Gq.pop(0)

            for dir in range(4):
                ny = y + dy[dir]
                nx = x + dx[dir]

                if 0 <= ny <= N-1 and 0 <= nx <= M-1 and arr[ny][nx] != 0 and visited[ny][nx] == 2500:
                    visited[ny][nx] = cnt
                    n_Gq.add((ny, nx))

        for i in range(len(Rq)):
            y, x = Rq.pop(0)

            for dir in range(4):
                ny = y + dy[dir]
                nx = x + dx[dir]

                if 0 <= ny <= N-1 and 0 <= nx <= M-1 and arr[ny][nx] != 0 and visited[ny][nx] >= cnt:
                    visited[ny][nx] = cnt
                    n_Rq.add((ny, nx))

        Gq = list(n_Gq - n_Rq)
        Rq = list(n_Rq - n_Gq)
        res += len(n_Gq) - len(Gq)

        cnt += 1

    ans = max(ans, res)


def make_queue(new_Gq, new_Rq, idx):
    global G, R
    if len(new_Gq) == G and len(new_Rq) == R:
        BFS(new_Gq, new_Rq)
        return

    if idx == len(feed):
        return

    if len(new_Gq) < G:
        new_Gq.append(feed[idx])
        make_queue(new_Gq, new_Rq, idx+1)
        new_Gq.pop()

    if len(new_Rq) < R:
        new_Rq.append(feed[idx])
        make_queue(new_Gq, new_Rq, idx + 1)
        new_Rq.pop()

    make_queue(new_Gq, new_Rq, idx + 1)

N, M, G, R = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
feed = []
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            feed.append((i, j))

ans = 0
make_queue([], [], 0)
print(ans)