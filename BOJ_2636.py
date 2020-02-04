def air(i, j):
    queue = [[i, j]]
    while queue:
        current = queue.pop(-1)
        y = current[0]
        x = current[1]
        arr[y][x] = 9
        for d in range(4):
            if 0 <= y + dy[d] <= N - 1 and 0 <= x + dx[d] <= M - 1:
                if arr[y + dy[d]][x + dx[d]] == 0:
                    queue.append([y + dy[d], x + dx[d]])

def new_air(i, j):
    global queue
    q = [[i, j]]
    new = []
    while q:
        current = q.pop(-1)
        y = current[0]
        x = current[1]
        arr[y][x] = 9
        new.append([y, x])
        for d in range(4):
            if 0 <= y + dy[d] <= N - 1 and 0 <= x + dx[d] <= M - 1:
                if arr[y + dy[d]][x + dx[d]] == 0:
                    q.append([y + dy[d], x + dx[d]])
    print("뉴!!!", new)
    queue += new


N, M = map(int,input().split())
arr = []
for i in range(N):
    arr.append(list(map(int,input().split())))

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

air(0, 0)

for __ in range(N):
    print(arr[__])
print()

queue = []

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            for d in range(4):
                if 0 <= i + dy[d] <= N - 1 and 0 <= j + dx[d] <= N - 1:
                    if arr[i + dy[d]][j + dx[d]] == 9:
                        queue.append([i, j])
                        break

# print(queue)

cnt = 0
while queue:
    last = len(queue)
    for _ in range(len(queue)):
        current = queue.pop(0)
        i = current[0]
        j = current[1]
        arr[i][j] = 9
        for d in range(4):
            if 0 <= i + dy[d] <= N - 1 and 0 <= j + dx[d] <= N - 1:
                if arr[i + dy[d]][j + dx[d]] == 1:
                    queue.append([i + dy[d], j + dx[d]])
                elif arr[i + dy[d]][j + dx[d]] == 0:
                    new_air(i + dy[d], j + dx[d])

    # for __ in range(N):
    #     print(arr[__])
    # print()
    # cnt += 1

print(cnt)
print(last)