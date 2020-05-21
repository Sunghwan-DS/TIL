import random

def cal_cnt(random_color, A, B):
    start, end = -1, -1
    low = 0
    high = len(record[random_color]) - 1

    # Lower_bound
    while low < high:
        m = (low + high) // 2
        # print(low, m, high)
        if record[random_color][m] > A:
            high = m
            start = m
        elif record[random_color][m] < A:
            low = m + 1
        else:
            start = m
            break
    if start == -1:
        start = low

    # upper_bound
    low = 0
    high = len(record[random_color]) - 1
    while low < high:
        m = (low + high) // 2
        # print(low, m, high)
        if record[random_color][m] > B:
            high = m - 1
        elif record[random_color][m] < B:
            end = m
            low = m + 1
        else:
            end = m
            break
    if record[random_color][low] == B:
        end = low
    if end == -1:
        end = high
    # print(low)
    # if nums[high] == target:
    #     end = high
    # print(random_color, start, end)
    # print(random_color, '시작', start, '끝', end)
    return end - start + 1


N, C = map(int, input().split())
caps = [0] + list(map(int, input().split()))
record = {}
for idx, color in enumerate(caps):
    if color not in record:
        record[color] = [idx]
    else:
        record[color].append(idx)
# print(record)
M = int(input())
for _ in range(M):
    A, B = map(int, input().split())
    check = (B - A + 1) // 2
    check_color = {}
    for _ in range(20):
        random_color = caps[random.choice([i for i in range(A, B+1)])]
        if random_color in check_color:
            continue
        else:
            check_color[random_color] = 1

        cnt = cal_cnt(random_color, A, B)
        # print(random_color, cnt, check)
        if cnt > check:
            print('yes', random_color)
            break
    else:
        print('no')