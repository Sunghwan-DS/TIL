def shutter(y, x, case):
    global n
    test_arr = [arr[i][:] for i in range(N)]
    for i in range(n):
        if cctv[i][3] == 1:




        elif cctv[i][3] == 2:





def cctv_set():
    for i in


N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
cctv = []
for i in range(N):
    for j in range(M):
        if arr[i][j] not in [0, 6]:
            cctv.append([i, j, arr[i][j]])

n = len(cctv)