import sys

def row_check(y, x):
    check = [False] * 10

    for j in range(9):
        if not check[arr[y][j]]:
            if arr[y][j] != 0:
                check[arr[y][j]] = True
        else:
            return False
    return True


def col_check(y, x):
    check = [False] * 10

    for i in range(9):
        if not check[arr[i][x]]:
            if arr[i][x] != 0:
                check[arr[i][x]] = True
        else:
            return False
    return True


def square_check(y, x):
    ny = y // 3
    nx = x // 3
    check = [False] * 10

    for i in range(3*ny, 3*ny+3):
        for j in range(3*nx, 3*nx+3):
            if not check[arr[i][j]]:
                if arr[i][j] != 0:
                    check[arr[i][j]] = True
            else:
                return False
    return True


def fill(idx):
    global N
    if idx == N:
        for i in range(9):
            print(*arr[i])
        sys.exit()

    y, x = zero[idx]
    can_fill = [False] + [True] * 9

    for k in range(9):
        can_fill[arr[y][k]] = False
        can_fill[arr[k][x]] = False

    ny = y // 3 * 3
    nx = x // 3 * 3

    for i in range(ny, ny+3):
        for j in range(nx, nx+3):
            can_fill[arr[i][j]] = False
    can_fill = [idx+1 for idx, i in enumerate(can_fill[1:]) if i]

    for num in can_fill:
        arr[y][x] = num
        fill(idx+1)
        arr[y][x] = 0


arr = [list(map(int,input().split())) for _ in range(9)]
zero = []

for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            zero.append((i, j))

N = len(zero)
fill(0)