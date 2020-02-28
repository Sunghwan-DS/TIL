# 2020.02.28
# 12:27 ~ 12:43
# 순열 구현

def make(val, idx):
    global N, min_ans, max_ans
    if idx == N:
        min_ans = min(min_ans, val)
        max_ans = max(max_ans, val)
        return

    if syms[0] > 0:
        syms[0] -= 1
        make(val + nums[idx], idx + 1)
        syms[0] += 1

    if syms[1] > 0:
        syms[1] -= 1
        make(val - nums[idx], idx + 1)
        syms[1] += 1

    if syms[2] > 0:
        syms[2] -= 1
        make(val * nums[idx], idx + 1)
        syms[2] += 1

    if syms[3] > 0:
        syms[3] -= 1
        if val >= 0:
            make(val // nums[idx], idx + 1)
        else:
            make(-((-val)//nums[idx]), idx + 1)
        syms[3] += 1


T = int(input())
for case in range(1, T+1):
    N = int(input())
    syms = list(map(int,input().split()))
    nums = list(map(int,input().split()))
    min_ans = 100000001
    max_ans = -100000001

    make(nums[0], 1)
    print("#%d"%(case), (max_ans - min_ans))