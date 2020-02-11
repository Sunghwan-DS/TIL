def BFS(lst):
    global ans
    q = []
    for idx in lst:
        q.append(virus[idx])
    visited = [[False] * N for _ in range(N)]
    new = [arr[i][:] for i in range(N)]
    for y, x in q:
        visited[y][x] = True
    result = 0
    while q:
        TF = True
        for c in range(len(q)):
            y, x = q.pop(0)

            for dir in range(4):
                ny = y + dy[dir]
                nx = x + dx[dir]

                if 0 <= ny <= N-1 and 0 <= nx <= N-1 and not visited[ny][nx]:
                    if new[ny][nx] == 0:
                        new[ny][nx] = 2
                        visited[ny][nx] = True
                        q.append((ny, nx))
                        TF = False

                    elif new[ny][nx] == 2:
                        visited[ny][nx] = True
                        q.append((ny, nx))

        if TF:
            break
        result += 1


    for i in range(N):
        for j in range(N):
            if new[i][j] == 0:
                return

    if ans > result:
        ans = result


def order(idx, lst):
    global cnt
    if len(lst) == M:
        BFS(lst)
        return


    for i in range(lst[-1]+1, len(virus)):
        if i not in lst:
            lst.append(i)
            order(idx + 1, lst)
            lst.pop()

N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
ans = 3000
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

virus = []
cnt = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            virus.append((i, j))
            cnt += 1

for i in range(len(virus)):
    order(1, [i])

if ans == 3000:
    print(-1)
else:
    print(ans)