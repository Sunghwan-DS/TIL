# 2020.11.29
# 21:00 ~ 21:25

dy = (0, -1, -1, 0, 1, 1, 1, 0, -1)
dx = (0, 0, -1, -1, -1, 0, 1, 1, 1)

field = [[0] * 4 for _ in range(4)]

for y in range(4):
    s0, d0, s1, d1, s2, d2, s3, d3 = map(int, input().split())
    field[y][0] = (s0, d0)
    field[y][1] = (s1, d1)
    field[y][2] = (s2, d2)
    field[y][3] = (s3, d3)

stack = [(0, 0)]
eat = field[0][0][0]
field[0][0] = (17, field[0][0][1])
answer = eat

def shark_go(y, x, eat):
    dirc = field[y][x][1]
    ori_field = field[:][:]
    update = False
    for distance in range(1, 4):
        ny = y + dy[dirc]
        nx = x + dx[dirc]
        if 0 <= ny < 4 and 0 <= nx < 4:
            if field[ny][nx]:
                now_eat = field[ny][nx][0]
                field[ny][nx] = (17, field[ny][nx][1])
                go(ny, nx, eat + now_eat)
                field = ori_field[:][:]
        else:
            break

shark_go(0)




