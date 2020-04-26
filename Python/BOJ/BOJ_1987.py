# python3 시간초과, pypy3 시간초과 (대략 80퍼센트)

def go(y, x, res):
    global ans, R, C
    if ans < res:
        ans = res
    for dirc in range(4):
        ny = y + dy[dirc]
        nx = x + dx[dirc]
        if 0 <= ny <= R-1 and 0 <= nx <= C-1 and not visited.get(arr[ny][nx]):
            visited[arr[ny][nx]] = 1
            go(ny, nx, res + 1)
            del visited[arr[ny][nx]]


dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

R, C = map(int,input().split())
arr = [(input()) for _ in range(R)]
ans = 0
visited = {}
visited[arr[0][0]] = 1
go(0, 0, 1)
print(ans)