def check(lst):
    i = 0
    for j in range(M):
        x = j
        while i != M:
            for dir in range(2):
                nx = j + LR[dir]
                if 0 <= nx <= N-1:
                    if lst[i][nx] = True:
                        x = 








def order(idx, pre):
    if idx == 3:
        check(pre)
    new = [pre[i][:] for i in range(M)]
    for i in range(M):
        for j in range(N-1):
            if new[i][j] == True
                continue
            else:
                new[i][j] = True
                order(idx+1, new)
                new[i][j] = False

LR = [-1, 0]






N, M, H = map(int,input().split())
arr = [[False] * (N-1) for _ in range(M)]
for j in range(M):
    a, b = map(int,input())
    arr[a-1][b-1] = True

order(0, arr)