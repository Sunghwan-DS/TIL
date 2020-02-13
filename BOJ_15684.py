def check(lst, res):
    global ans
    for j in range(N):
        x = j
        i = 0
        while i < H:
            if x-1 >= 0 and lst[i][x-1]:
                x -= 1
            elif x+1 <= N-1 and lst[i][x]:
                x += 1
            i += 1
        if j == x:
            pass
        else:
            return

    if ans > res:
        ans = res


def order(idx, pre, save):
    if idx == 0:
        check(pre, idx)

    if idx == 1:
        check(pre, idx)

    if idx == 2:
        check(pre, idx)

    if idx == 3:
        check(pre, idx)
        return

    for i in range(save, H):
        for j in range(N-1):
            if pre[i][j]:
                continue
            if j+1 <= N-2 and pre[i][j+1]:
                continue
            if j-1 >= 0 and pre[i][j-1]:
                continue
            else:
                pre[i][j] = True
                order(idx+1, pre, i)
                pre[i][j] = False


N, M, H = map(int,input().split())
arr = [[False] * (N-1) for _ in range(H)]

for j in range(M):
    a, b = map(int,input().split())
    arr[a-1][b-1] = True

ans = 4
order(0, arr, 0)

if ans == 4:
    print(-1)
else:
    print(ans)