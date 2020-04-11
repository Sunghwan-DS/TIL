dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def BFS():
    global w, h, q
    ans = 0
    nq = []
    while q:
        ans += 1
        for i in range(len(q)):
            y, x, d = q.pop()

            for dir in range(4):
                ny = y + dy[dir]
                nx = x + dx[dir]

                if 0 <= ny <= h-1 and 0 <= nx <= w-1:
                    if not visited[ny][nx] and arr[ny][nx] != '#':
                        visited[ny][nx] = True
                        if d == 1:
                            nq.insert(0, (ny, nx, d))
                        else:
                            nq.append((ny, nx, d))
                elif d == 1:
                    return ans
        q = nq[:]
        nq = []
    return "IMPOSSIBLE"

for tc in range(int(input())):
    w, h = map(int,input().split())
    arr = [list(input()) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    q = []

    for i in range(h):
        for j in range(w):
            if arr[i][j] == '*':
                q.append((i, j, 0))
                visited[i][j] = True
            elif arr[i][j] == '@':
                q.insert(0, (i, j, 1))
                visited[i][j] = True
    print(BFS())