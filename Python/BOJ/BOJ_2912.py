# 시간초과
# 시간복잡도: 300000 + 10000 * 300000 + 10000 * 2 * 10000 = 300,000 + 30억 + 2억 => 32 초 X

import copy
import sys
input = sys.stdin.readline
N, C = map(int, input().split())
data = list(map(int, input().split()))
M = int(input())

record = [0] * (N+1)
record[0] = {}
rec = {}
for idx, d in enumerate(data):
    if d in rec:
        rec[d] += 1
    else:
        rec[d] = 1
    record[idx + 1] = copy.deepcopy(rec)

for _ in range(M):
    A, B = map(int, input().split())
    for num in record[B]:
        if num in record[A-1]:
            num_A = record[A-1][num]
        else:
            num_A = 0
        num_B = record[B][num]
        if num_B - num_A > (B-A+1) / 2:
            print('yes', num)
            break
    else:
        print('no')