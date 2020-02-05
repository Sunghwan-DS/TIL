def level_up():
    global size, eat
    if size == eat:
        size += 1
        eat = 0
    return


N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

for i in range(N):
    TF = False
    for j in range(N):
        if arr[i][j] == 9:
            s_y = i
            s_x = j
            TF = True
            break
    if TF:
        break

dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]
size = 2
eat = 0
queue = [[i,j]]
arr[i][j] = 0
cnt = 0
cnt2 = 0
visited = [[False] * N for _ in range(N)]
visited[i][j] = True
while queue:
    cnt2 += 1
    eat_lst = []
    TF = False
    for i in range(len(queue)):
        current = queue.pop(0)
        y = current[0]
        x = current[1]
        for dir in range(4):
            ny = y+dy[dir]
            nx = x+dx[dir]
            if 0 <= ny <= N-1 and 0 <= nx <= N-1 and arr[ny][nx] <= size and not visited[ny][nx]:
                if 0 < arr[ny][nx] < size:
                    eat_lst.append([ny,nx])
                    visited[ny][nx] = True
                else:
                    visited[ny][nx] = True
                    queue.append([ny,nx])

    if not eat_lst == []:
        eat_y = N-1
        eat_x = N-1
        for e in eat_lst:
            if e[0] < eat_y:
                eat_y = e[0]
                eat_x = e[1]
            elif e[0] == eat_y:
                if e[1] <eat_x:
                    eat_x =e[1]

        eat += 1
        level_up()
        queue = [[eat_y, eat_x]]
        cnt += cnt2
        cnt2 = 0
        arr[eat_y][eat_x] = 0
        visited = [[False] * N for _ in range(N)]
        visited[eat_y][eat_x] = True

print(cnt)