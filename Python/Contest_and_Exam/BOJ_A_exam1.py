# 2020.03.21
# 14:00 ~ 14:41
# 시뮬레이션 구현
#

N, M, K = map(int,input().split())
arr = [[0] * M for _ in range(N)]

for sticky_num in range(K):
    R, C = map(int,input().split())
    sticker = [list(map(int,input().split())) for _ in range(R)]
    find = False
    for dir in range(4):
        for i in range(N-R+1):
            for j in range(M-C+1):
                new_arr = [arr[_][:] for _ in range(N)]
                stop = False
                for ii in range(R):
                    for jj in range(C):
                        if new_arr[i+ii][j+jj] and sticker[ii][jj]:
                            stop = True
                            break
                        elif new_arr[i+ii][j+jj] or sticker[ii][jj]:
                            new_arr[i+ii][j+jj] = 1

                    if stop:
                        break
                else:
                    arr = new_arr
                    find = True
                    break

            if find:
                break

        if find:
            break
        else:
            sticker = [[sticker[j][i] for j in range(R-1, -1, -1)] for i in range(C)]
            R, C = C, R

ans = 0
for i in range(N):
    ans += sum(arr[i])

print(ans)