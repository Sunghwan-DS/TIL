def counting():
    new_arr = []
    cnt = 0
    for _ in range(N):
        new_arr.append(arr[_])
    for i in range(N):
        for j in range(N):
            if new_arr[i][j] != 0:
                cnt += 1
                queue = [[i, j]]
                while queue:
                    current = queue.pop(-1)
                    y = current[0]
                    x = current[1]
                    new_arr[y][x] = 0
                    for dir in range(4):
                        if 0 <= y+dy[dir] <= N-1 and 0 <= x+dx[dir] <= N-1:
                            if new_arr[y+dy[dir]][x+dx[dir]] != 0:
                                queue.append([y+dy[dir], x+dx[dir]])
    return cnt

N = int(input())
arr = []
rain = []
table = [[] * 101]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
for i in range(N):
    arr.append(list(map(int,input().split())))
    for j in range(N):
        if arr[i][j] not in rain:
            rain.append(arr[i][j])
        table[arr[i][j]].append([i, j])
rain.sort()

visited = [False * N for _ in range(N)]

result = 0

for i in rain:
    cnt = 0
    for j in table[i]:
        arr[j[0]][j[1]] = 0
    t = counting()
    if result < t:
        result = t

print(result)
