# 2020.03.05
# 13:17 ~ 16:25
# 전역탐색
# python3, pypy3 시간 초과

import sys
from itertools import permutations

def cal(lst):
    global N
    runner1, runner2, runner3 = 0, 0, 0
    out = 0
    score = 0
    inning = 0
    idx = 0
    while inning != N:
        if arr[inning][lst[idx]] == 0:
            out += 1
            if out == 3:
                out = 0
                inning += 1
                runner1, runner2, runner3 = 0, 0, 0

        elif arr[inning][lst[idx]] == 1:
            score += runner3
            runner1, runner2, runner3 = 1, runner1, runner2

        elif arr[inning][lst[idx]] == 2:
            score += runner2 + runner3
            runner1, runner2, runner3 = 0, 1, runner1

        elif arr[inning][lst[idx]] == 3:
            score += runner1 + runner2 + runner3
            runner1, runner2, runner3 = 0, 0, 1

        elif arr[inning][lst[idx]] == 4:
            score += runner1 + runner2 + runner3 + 1
            runner1, runner2, runner3 = 0, 0, 0

        idx = (idx+1) % 9
    return score


N = int(sys.stdin.readline())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
ans = 0

for seq in permutations([i for i in range(1, 9)], 8):
    lst = list(seq[:3]) + [0] + list(seq[3:])
    ans = max(ans, cal(lst))

print(ans)