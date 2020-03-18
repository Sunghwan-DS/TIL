# 2020.03.18
# 15:50 ~ 16:22
# 시뮬레이션 구현
# 시간:68mx, 코드 길이:1151B

N = int(input())
K = int(input())
arr = [[0] * N for _ in range(N)]
for i in range(K):
    y, x = map(int,input().split())
    arr[y-1][x-1] = 1

L = int(input())

y, x, dir = 0, 0, 0
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
body = [(0, 0)]
ans = 0

for i in range(L):
    X, C = input().split()
    X = int(X)
    last_ans = ans
    for j in range(X - last_ans):
        head_y, head_x = body[-1]
        ans += 1
        ny, nx = head_y + dy[dir], head_x + dx[dir]
        if 0 <= ny <= N-1 and 0 <= nx <= N-1 and (ny, nx) not in body:
            if arr[ny][nx] == 1:
                arr[ny][nx] = 0
            else:
                body.pop(0)
            body.append((ny, nx))
        else:
            print(ans)
            exit()

    if C == "L":
        dir += 3
        dir %= 4
    elif C == "D":
        dir += 1
        dir %= 4

head_y, head_x = body[-1]
ny, nx = head_y + dy[dir], head_x + dx[dir]
ans += 1
while 0 <= ny <= N-1 and 0 <= nx <= N-1 and (ny, nx) not in body:
    if arr[ny][nx] == 1:
        arr[ny][nx] = 0
    else:
        body.pop()
    body.append((ny, nx))
    ans += 1
    ny += dy[dir]
    nx += dx[dir]

print(ans)