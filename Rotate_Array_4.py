N, M, K = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
new_arr = [[0] * M for _ in range(N)]
rcs = []
answer = []
for i in range(N):
    for j in range(M):
        new_arr[i][j] = arr[i][j]

def rotation(r, c, s, arr):
    global new_arr
    for i in range(N):
        for j in range(M):
            new_arr[i][j] = arr[i][j]

    for shell in range(1, s+1):
        for x in range(2*shell):
            new_arr[r-shell-1+x][c-shell-1] = arr[r-shell+x][c-shell-1]

        for x in range(2*shell):
            new_arr[r+shell-1][c-shell-1+x] = arr[r+shell-1][c-shell+x]

        for x in range(2*shell):
            new_arr[r+shell-1-x][c+shell-1] = arr[r+shell-2-x][c+shell-1]

        for x in range(2*shell):
            new_arr[r-shell-1][c+shell-1-x] = arr[r-shell-1][c+shell-2-x]


def sequence(index, K, table):
    global answer
    if index == K:
        r = rcs[table[0]][0]
        c = rcs[table[0]][1]
        s = rcs[table[0]][2]
        rotation(r, c, s, arr)

        for __ in range(1, K):
            r = rcs[table[__]][0]
            c = rcs[table[__]][1]
            s = rcs[table[__]][2]
            rotation(r, c, s, new_arr)

        result = sum(new_arr[0])
        for idx in range(1, N):
            if result > sum(new_arr[idx]):
                result = sum(new_arr[idx])

        answer.append(result)
        return

    for _ in range(K):
        if _ in table:
            continue
        table.append(_)
        sequence(index+1, K, table)
        table.remove(_)


for _ in range(K):
    r, c, s = map(int, input().split())
    rcs.append([r, c, s])

sequence(0, K, [])

print(min(answer))