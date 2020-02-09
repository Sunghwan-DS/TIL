def shutter(y, x, case):
    global n
    new_arr = [arr[i][:] for i in range(N)]
    for i in range(n):
        if cctv[i][3] == 1:




        elif cctv[i][3] == 2:





def cctv_set(idx, lst):
    if idx == n+1:
        shutter(lst)

    for d in range(4):
        lst.append(d)
        cctv_set(idx+1, lst)
        lst.pop(-1)


N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
cctv = []
for i in range(N):
    for j in range(M):
        if arr[i][j] not in [0, 6]:
            cctv.append([i, j, arr[i][j]])

n = len(cctv)
cctv_set(0, [])