def issafe(val):
    global N
    if 0 <= val <= N-1:
        return True
    else:
        return False


def check(cur):
    global N
    y = cur // N
    x = cur % N

    for dirc in range(2):
        ny, nx = y, x
        while issafe(ny + dy[dirc]) and issafe(nx + dx[dirc]):
            ny += dy[dirc]
            nx += dx[dirc]
            if visited[ny][nx]:
                return False
    return True


def make(cur, res):
    global N, ans
    if cur == N ** 2:
        ans = max(ans, res)
        if ans == 2*N - 2:
            print(ans)
            exit()
        return

    # for idx in range(cur, N**2):
    #     if arr[idx // N][idx % N] == 1:
    #         if check(idx):
    #             visited[idx // N][idx % N] = True
    #             make(idx+1, res+1)
    #             visited[idx // N][idx % N] = False

    for idx in range(cur, len(Bishop)):
        if check

dy = [-1, -1]
dx = [-1, 1]

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
# Black = []
# White = []
Bishop = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            # if i+j % 2 == 0:
            #     Black.append((i, j))
            # else:
            #     White.append((i, j))
            Bishop.append((i, j))
ans = 0
make(0, 0)
print(ans)