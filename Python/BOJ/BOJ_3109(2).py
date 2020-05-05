def DFS(y, x):
    global C
    if x == C-1:
        return 1

    for dy in (-1, 0, 1):
        ny = y + dy
        if 0 <= ny <= R-1 and arr[ny][x+1] == '.':
            arr[ny][x+1] = 'x'
            if DFS(ny, x+1):
                return 1
    return 0


R, C = map(int,input().split())
arr = [list(input()) for _ in range(R)]

ans = 0
for i in range(R):
    ans += DFS(i, 0)

print(ans)