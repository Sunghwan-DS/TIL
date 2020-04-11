def rotation(x, d, k):
    global N, M
    for i in range(N):
        if (i+1) % x == 0:
            if d == 0:
                for _ in range(k):
                    a = arr[i].pop(-1)
                    arr[i].insert(0, a)

            elif d == 1:
                for _ in range(k):
                    a = arr[i].pop(0)
                    arr[i].append(a)

    lst = []
    for i in range(N - 1):
        for j in range(M):
            if arr[i][j] == arr[i + 1][j] and arr[i][j] != 0:
                lst.append([i, j])
                lst.append([i + 1, j])

    for i in range(N):
        for j in range(M):
            if arr[i][j - 1] == arr[i][j] and arr[i][j - 1] != 0:
                lst.append([i, j - 1])
                lst.append([i, j])

    if len(lst) == 0:
        cnt = 0
        tot = 0
        for i in range(N):
            for j in range(M):
                if arr[i][j] != 0:
                    tot += arr[i][j]
                    cnt += 1

        if cnt == 0:
            return

        avg = tot / cnt
        for i in range(N):
            for j in range(M):
                if arr[i][j] != 0:
                    if arr[i][j] > avg:
                        arr[i][j] -= 1
                    elif arr[i][j] < avg:
                        arr[i][j] += 1
    else:
        for co in lst:
            arr[co[0]][co[1]] = 0


N, M, T = map(int,input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int,input().split())))

for _ in range(T):
    W, d, k = map(int, input().split())
    rotation(W, d, k)

result = 0
for i in range(N):
    result += sum(arr[i])


print(result)