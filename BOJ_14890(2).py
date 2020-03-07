# 2020.03.07
# 21:40 ~ 21:50
# 시뮬레이션 구현
# 시간:64ms, 코드 길이:1032B

N, L = map(int,input().split())
arr =[list(map(int,input().split())) for _ in range(N)]
ans = 0
for i in range(N):
    cnt = 1
    for j in range(N-1):
        if arr[i][j] == arr[i][j+1]:
            cnt += 1
        elif arr[i][j]+1 == arr[i][j+1]:
            if cnt >= L:
                cnt = 1
            else:
                break
        elif arr[i][j]-1 == arr[i][j+1]:
            if cnt >= 0:
                cnt = -L+1
            else:
                break
        else:
            break
    else:
        if cnt >= 0:
            ans += 1

for j in range(N):
    cnt = 1
    for i in range(N-1):
        if arr[i][j] == arr[i+1][j]:
            cnt += 1
        elif arr[i][j]+1 == arr[i+1][j]:
            if cnt >= L:
                cnt = 1
            else:
                break
        elif arr[i][j]-1 == arr[i+1][j]:
            if cnt >= 0:
                cnt = -L + 1
            else:
                break
        else:
            break
    else:
        if cnt >= 0:
            ans += 1

print(ans)