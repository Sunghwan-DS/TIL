# 2020.03.05
# 16:32 ~ 17:03
# 시뮬레이션 구현
# 시간:60ms, 코드 길이:671B

N = int(input())
arr = [[0] * 101 for _ in range(101)]
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

for n in range(1, N+1):
    x, y, d, g = map(int,input().split())
    arr[y][x] = n
    history = [d]
    y += dy[d]
    x += dx[d]
    arr[y][x] = n
    generation = 1

    while generation <= g:
        for idx in range(len(history) - 1, -1, -1):
            nd = (history[idx] + 1) % 4
            y += dy[nd]
            x += dx[nd]
            arr[y][x] = n
            history.append(nd)
        generation += 1

ans = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] and arr[i][j+1] and arr[i+1][j] and arr[i+1][j+1]:
            ans += 1

print(ans)