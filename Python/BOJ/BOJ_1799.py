def issafe(val):
    global N
    if 0 <= val <= N-1:
        return True
    else:
        return False


def marking(tu):
    global N
    y = tu[0]
    x = tu[1]
    visited[y][x] = True
    save = []
    save.append((y, x))
    for dirc in range(4):
        ny, nx = y, x
        while issafe(ny + dy[dirc]) and issafe(nx + dx[dirc]):
            ny += dy[dirc]
            nx += dx[dirc]
            if not visited[ny][nx]:
                save.append((ny, nx))
                visited[ny][nx] = True
    return save


def make(cur, res, board):
    global N, ans
    if ans < res:
        if res == 2 * N - 2:
            print(res)
            exit()
        else:
            ans = res
    if cur == len(board):
        return

    for idx in range(cur, len(board)):
        if not visited[board[idx][0]][board[idx][1]]:
            save = marking(board[idx])
            make(idx+1, res+1)
            for y, x in save:
                visited[y][x] = False


dy = [-1, -1, 1, 1]
dx = [-1, 1, -1, 1]

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
Black = []
White = []
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            if (i + j) % 2:
                Black.append((i, j))
            else:
                White.append((i, j))

visited = [[False] * N for _ in range(N)]
ans = 0
make(0, 0)
print(ans)