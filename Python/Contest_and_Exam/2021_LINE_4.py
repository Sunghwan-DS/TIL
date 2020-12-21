# 10:43 ~ 11:16

def solution(maze):
    def issafe(y, x, goal):
        if 0 <= y <= goal and 0 <= x <= goal:
            return True
        else:
            return False

    goal = len(maze) - 1
    dy = (0, 1, 0, -1)
    dx = (1, 0, -1, 0)
    dirc = 1

    y = 0
    x = 0

    left = (dirc + 3) % 4
    Ly = y + dy[left]
    Lx = x + dx[left]
    if not maze[Ly][Lx]:
        dirc = 0

    cnt = 0
    while not (y == goal and x == goal):
        y = y + dy[dirc]
        x = x + dx[dirc]
        cnt += 1
        left = (dirc + 3) % 4
        Ly = y + dy[left]
        Lx = x + dx[left]
        Ny = y + dy[dirc]
        Nx = x + dx[dirc]

        if issafe(Ly, Lx, goal) and not maze[Ly][Lx]:
            dirc = left
        elif not issafe(Ny, Nx, goal) or maze[Ny][Nx]:
            right = (dirc + 1) % 4
            dirc = right
            Ny = y + dy[dirc]
            Nx = x + dx[dirc]

            if not issafe(Ny, Nx, goal) or maze[Ny][Nx]:
                right = (dirc + 1) % 4
                dirc = right

    answer = cnt
    return answer

ex1 = [[0, 1, 0, 1], [0, 1, 0, 0], [0, 0, 0, 0], [1, 0, 1, 0]] # ans = 10
ex2 = [[0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 1, 0], [0, 1, 0, 0, 1, 0], [0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0]] # ans = 32
ex3 = [[0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0]] # ans = 24

print(solution(ex3))