# 2020.03.21
# 22:00 ~ 22:32
# BFS 구현
# 시간:1004ms, 코드 길이:1810B

def BFS(virus):
    global ans
    visited = [[False] * N for _ in range(N)]
    q = virus[:]
    for y, x in q:
        visited[y][x] = True

    final_cnt = 2500
    res = 0
    cnt = 0
    stop = False
    while q:
        cnt += 1
        for _ in range(len(q)):
            y, x = q.pop(0)

            for dir in range(4):
                ny = y + dy[dir]
                nx = x + dx[dir]

                if 0 <= ny <= N-1 and 0 <= nx <= N-1 and not visited[ny][nx] and arr[ny][nx] != 1:
                    q.append((ny, nx))
                    visited[ny][nx] = True
                    if arr[ny][nx] == 0:
                        res += 1
                        if res == need:
                            final_cnt = cnt
                            stop = True
                            break
            if stop:
                break
        if stop:
            break

    stop = False
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and arr[i][j] == 0:
                stop = True
                break
        if stop:
            break
    else:
        ans = min(ans, final_cnt)


def make_virus(idx, virus):
    if len(virus) == M:
        BFS(virus)
        return

    if idx == len(virus_co):
        return

    virus.append(virus_co[idx])
    make_virus(idx + 1, virus)
    virus.pop()
    make_virus(idx + 1, virus)


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
need = 0
virus_co = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            virus_co.append((i, j))
        elif arr[i][j] == 0:
            need += 1

if need == 0:
    print(0)
    exit()

ans = 2500
make_virus(0, [])

if ans == 2500:
    print(-1)
else:
    print(ans)