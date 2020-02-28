# 2020.02.28
# 12:27 ~ 12:43
# 순열 구현
# 시간:458ms, 코드 길이:923B

def make(val, idx, lst):
    global N, min_ans, max_ans
    if idx == N:
        min_ans = min(min_ans, val)
        max_ans = max(max_ans, val)
        return

    if lst[0] > 0:
        lst[0] -= 1
        make(val+nums[idx], idx+1, lst)
        lst[0] += 1

    if lst[1] > 0:
        lst[1] -= 1
        make(val-nums[idx], idx+1, lst)
        lst[1] += 1

    if lst[2] > 0:
        lst[2] -= 1
        make(val*nums[idx], idx+1, lst)
        lst[2] += 1

    if lst[3] > 0:
        lst[3] -= 1
        if val >= 0:
            make(val//nums[idx], idx+1, lst)
        else:
            make(-((-val)//nums[idx]), idx+1, lst)
        lst[3] += 1


T = int(input())
for case in range(1, T+1):
    N = int(input())
    syms = list(map(int,input().split()))
    nums = list(map(int,input().split()))
    min_ans = 100000001
    max_ans = -100000001

    make(nums[0], 1, syms)
    print("#%d"%(case), (max_ans - min_ans))