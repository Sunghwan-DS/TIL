def move(lst, arr):
    global N
    for dir in lst:
        if dir == 0:
            for j in range(N):
                s = 0
                cnt_i = 0
                for i in range(N):
                    if arr[i][j] != 0:
                        if s != arr[i][j]:
                            pre = arr[i][j]
                            arr[i][j] = 0
                            arr[cnt_i][j] = pre
                            s = pre
                            cnt_i += 1
                        elif s == arr[i][j]:
                            arr[cnt_i - 1][j] = s * 2
                            arr[i][j] = 0
                            s = 0
        elif dir == 2:
            for j in range(N):
                s = 0
                cnt_i = N-1
                for i in range(N-1, -1, -1):
                    if arr[i][j] != 0:
                        if s != arr[i][j]:
                            pre = arr[i][j]
                            arr[i][j] = 0
                            arr[cnt_i][j] = pre
                            s = pre
                            cnt_i -= 1
                        elif s == arr[i][j]:
                            arr[cnt_i + 1][j] = s * 2
                            arr[i][j] = 0
                            s = 0

        elif dir == 1:
            for i in range(N):
                s = 0
                cnt_j = N-1
                for j in range(N-1, -1, -1):
                    if arr[i][j] != 0:
                        if s != arr[i][j]:
                            pre = arr[i][j]
                            arr[i][j] = 0
                            arr[i][cnt_j] = pre
                            s = pre
                            cnt_j -= 1
                        elif s == arr[i][j]:
                            arr[i][cnt_j + 1] = s * 2
                            arr[i][j] = 0
                            s = 0

        elif dir == 3:
            for i in range(N):
                s = 0
                cnt_j = 0
                for j in range(N):
                    if arr[i][j] != 0:
                        if s != arr[i][j]:
                            pre = arr[i][j]
                            arr[i][j] = 0
                            arr[i][cnt_j] = pre
                            s = pre
                            cnt_j += 1
                        elif s == arr[i][j]:
                            arr[i][cnt_j - 1] = s * 2
                            arr[i][j] = 0
                            s = 0


def order(idx, lst):
    global N, ans
    if idx == 4:
        arr = [arr_init[_][:] for _ in range(N)]
        move(lst, arr)
        result = 0
        for i in range(N):
            for j in range(N):
                if arr[i][j] > result:
                    result = arr[i][j]
        if ans < result:
            ans = result
        return

    for i in range(4):
        lst.append(i)
        order(idx+1, lst)
        lst.pop()


N = int(input())
arr_init = [list(map(int,input().split())) for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
ans = 0

for i in range(4):
    order(0, [i])


print(ans)