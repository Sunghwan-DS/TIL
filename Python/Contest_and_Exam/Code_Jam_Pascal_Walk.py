def add_val(y, x):
    val = 1
    for i in range(y-x+1, y):
        val *= i
    for i in range(2, x):
        val /= i
    return val

def DFS(y, x, res, road):
    global N, find_ans, ans
    if find_ans or res > N or len(road) > 500:
        return

    if res == N:
        ans = road[:]
        find_ans = True
        return

    for dirc in range(6):
        ny = y + dy[dirc]
        nx = x + dx[dirc]

        if ny >= nx and nx >= 1 and not visited[ny][nx]:
            visited[ny][nx] = True
            road.append((ny, nx))
            DFS(ny, nx, res+add_val(ny, nx), road)
            visited[ny][nx] = False
            road.pop()


dy = [-1, -1, 0, 0, 1, 1]
dx = [-1, 0, -1 ,1, 0, 1]

for tc in range(1, int(input())+1):
    N = int(input())
    visited = [[False] * (i+1) for i in range(N+1)]
    visited[1][1] = True
    find_ans = False
    ans = []
    DFS(1, 1, 1, [(1, 1)])
    print("Case #%d:"%(tc))
    for y, x in ans:
        print(y, x)