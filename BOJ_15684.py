import sys
sys.setrecursionlimit(10**6)

def check(lst, res):
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

    print(res)
    sys.exit()


def order1(idx, pre):
    if idx == 1:
        check(pre, 1)
        return
    for i in range(H):
        for j in range(N-1):
            if pre[i][j]:
                continue
            else:
                pre[i][j] = True
                order1(idx+1, pre)
                pre[i][j] = False

def order2(idx, pre):
    if idx == 2:
        check(pre, 2)
        return
    for i in range(H):
        for j in range(N-1):
            if pre[i][j]:
                continue
            else:
                pre[i][j] = True
                order2(idx+1, pre)
                pre[i][j] = False

def order3(idx, pre):
    if idx == 3:
        check(pre, 3)
        return
    for i in range(H):
        for j in range(N-1):
            if pre[i][j]:
                continue
            else:
                pre[i][j] = True
                order3(idx+1, pre)
                pre[i][j] = False


N, M, H = map(int,input().split())
arr = [[False] * (N-1) for _ in range(H)]

for j in range(M):
    a, b = map(int,input().split())
    arr[a-1][b-1] = True

check(arr, 0)
order1(0, arr)
order2(0, arr)
order3(0, arr)

print(-1)