# 2020.02.21
# 10:34 ~ 10:45
# 브루트 포스, itertools 사용 (=> 3중for문으로도 간단하게 구현 가능)
# 시간:104ms, 코드 길이: 365B

from itertools import combinations as cb

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

lst = list(cb([i for i in range(5)], 3))
max_num = -1

for i in range(N):
    for a, b, c in lst:
        res = arr[i][a] + arr[i][b] + arr[i][c]
        if max_num <= res % 10:
            max_num = res % 10
            winner = i+1

print(winner)