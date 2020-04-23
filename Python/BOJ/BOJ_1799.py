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
        ans = res
    if cur == len(board):
        return

    while cur < len(board) - (ans - res):
        if not visited[board[cur][0]][board[cur][1]]:
            save = marking(board[cur])
            make(cur+1, res+1, board)
            for y, x in save:
                visited[y][x] = False
        cur += 1


def make2(cur, res, board):
    global N, ans2
    if ans2 < res:
        ans2 = res
    if cur == len(board):
        return

    while cur < len(board) - (ans2 - res):
        if not visited[board[cur][0]][board[cur][1]]:
            save = marking(board[cur])
            make2(cur+1, res+1, board)
            for y, x in save:
                visited[y][x] = False
        cur += 1


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
make(0, 0, Black)
ans2 = 0
make2(0, 0, White)
print(ans + ans2)