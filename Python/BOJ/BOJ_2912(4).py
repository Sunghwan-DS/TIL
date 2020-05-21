import sys
import random
input = sys.stdin.readline

def cal(start, end, idx, A, B, num):
    if A <= start and end <= B:
        if num in segmentTree[idx]:
            return segmentTree[idx][num]
        else:
            return 0

    if end < A or B < start:
        return 0

    res = 0
    mid = (start + end) // 2
    res += cal(start, mid, idx * 2, A, B, num)
    res += cal(mid + 1, end, idx * 2 + 1, A, B, num)
    return res


def make(start, end, idx):
    record = {}
    if start == end:
        record[data[start - 1]] = 1
        segmentTree[idx] = record
        return record

    mid = (start + end) // 2
    left = make(start, mid, idx * 2)
    right = make(mid + 1, end, idx * 2 + 1)

    for num in left:
        if num in record:
            record[num] += left[num]
        else:
            record[num] = left[num]

    for num in right:
        if num in record:
            record[num] += right[num]
        else:
            record[num] = right[num]

    segmentTree[idx] = record
    return record


N, C = map(int, input().split())
data = list(map(int, input().split()))
M = int(input())
segmentTree = [{} for _ in range(1048562)]
make(1, N, 1)
for _ in range(M):
    A, B = map(int, input().split())
    check = (B - A + 1) // 2

    check_color = {}
    for _ in range(20):
        random_color = data[random.choice([i for i in range(A, B + 1)]) - 1]
        if random_color in check_color:
            continue
        else:
            check_color[random_color] = 1
        if cal(1, N, 1, A, B, random_color) > check:
            print('yes', random_color)
            break
    else:
        print('no')