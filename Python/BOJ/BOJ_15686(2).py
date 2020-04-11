# 2020.03.05
# 12:47 ~ 13:08
# 전역탐색
# 시간:660ms, 코드 길이:569B
from itertools import combinations

N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
chicken = []
house = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            house.append((i, j))
        elif arr[i][j] == 2:
            chicken.append((i, j))

ans = 1000000
for lst in combinations(chicken, M):
    res = 0
    for y, x in house:
        min_res = 1000000
        for cy, cx in lst:
            min_res = min(min_res, abs(cy-y)+abs(cx-x))
        res += min_res
    ans = min(ans, res)
print(ans)