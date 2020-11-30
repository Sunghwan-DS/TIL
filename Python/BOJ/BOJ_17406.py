# 2020.11.30
# 13:20 ~ 13:56

N, M, K = map(int, input().split())
arr = []
for _ in range(N):
    row = list(map(int, input().split()))
    arr.append(row)

rotations = []
for _ in range(K):
    r, c, s = map(int, input().split())
    rotations.append((r-1, c-1, s))

visited = [False] * K
answer = 10 ** 9


def action(r, c, s):
    for d in range(1, s + 1):
        save = arr[r - d][c - d]
        for i in range(r - d, r + d):
            arr[i][c - d] = arr[i + 1][c - d]
        for j in range(c - d, c + d):
            arr[r + d][j] = arr[r + d][j + 1]
        for i in range(r + d, r - d, -1):
            arr[i][c + d] = arr[i - 1][c + d]
        for j in range(c + d, c - d, -1):
            arr[r - d][j] = arr[r - d][j - 1]
        arr[r - d][c - d + 1] = save


def backup(r, c, s):
    for d in range(1, s + 1):
        save = arr[r - d][c - d]
        for j in range(c - d, c + d):
            arr[r - d][j] = arr[r - d][j + 1]
        for i in range(r - d, r + d):
            arr[i][c + d] = arr[i + 1][c + d]
        for j in range(c + d, c - d, -1):
            arr[r + d][j] = arr[r + d][j - 1]
        for i in range(r + d, r - d, -1):
            arr[i][c - d] = arr[i - 1][c - d]
        arr[r - d + 1][c - d] = save


def rotation():
    global answer
    if False not in visited:
        for i in range(N):
            answer = min(answer, sum(arr[i]))
        return

    for idx in range(K):
        if not visited[idx]:
            r, c, s = rotations[idx]
            visited[idx] = True
            action(r, c, s)

            rotation()

            visited[idx] = False
            backup(r, c, s)

rotation()
print(answer)