# 2020.03.11
# 18:59 ~ 19:19
# 전탐
# 시간:167ms, 코드 길이:853B

for tc in range(1, int(input())+1):
    N, M = map(int,input().split())
    arr = [list(input()) for _ in range(N)]
    ans = 0
    line_data = []

    for i in range(N):
        W, B, R = 0, 0, 0

        for j in range(M):
            if arr[i][j] == "W":
                W += 1
            elif arr[i][j] == "B":
                B += 1
            else:
                R += 1
        line_data.append((W, B, R))

    max_res = 0
    for white in range(N-2):
        for blue in range(white+1, N-1):
            res = 0
            for i in range(white+1):
                res += line_data[i][0]
            for i in range(white+1, blue+1):
                res += line_data[i][1]
            for i in range(blue+1, N):
                res += line_data[i][2]

            max_res = max(max_res, res)

    print("#%d"%(tc), N*M-max_res)
