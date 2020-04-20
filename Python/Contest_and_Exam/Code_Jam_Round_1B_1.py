from collections import deque

def BFS():
    global X, Y
    q = deque()
    q.append(['', -X, -Y])
    while q:
        for i in range(len(q)):
            res, x, y = q.popleft()

            for dirc in range(4):
                ny = y + dy[dirc]
                nx = x + dx[dirc]

                if ny % 2 == 0 and nx % 2 == 0:
                    ny //= 2
                    nx //= 2
                    if (ny + nx) % 2 == 1:
                        q.append([res + d[dirc], nx, ny])
                    elif ny == 0 and nx == 0:
                        return res + d[dirc]


d = ('N', 'E', 'S', 'W')
dy = (1, 0, -1, 0)
dx = (0, 1, 0, -1)

for tc in range(1, int(input())+1):
    X, Y = map(int,input().split())
    ans = ''
    if (abs(X) + abs(Y)) % 2 ==  0:
        print("Case #%d:"%(tc), 'IMPOSSIBLE')
    else:
        print("Case #%d:"%(tc), BFS())