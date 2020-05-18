# 시간초과
# 시간복잡도: 1048562 * 2 * 4300(10000에서 평균 계산) + 재귀 깊이 20 * 10000 * 10000 = 90억 + 20억 = 110초

import sys
# sys.stdin = open('in.txt','r')
input = sys.stdin.readline

def cal(start, end, idx, A, B):
    if A <= start and end <= B:
        for num in segmentTree[idx]:
            if num in result:
                result[num] += segmentTree[idx][num]
            else:
                result[num] = segmentTree[idx][num]
        return

    if end < A or B < start:
        return

    mid = (start + end) // 2
    cal(start, mid, idx * 2, A, B)
    cal(mid + 1, end, idx * 2 + 1, A, B)
    return


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
    result = {}
    cal(1, N, 1, A, B)
    check = (B - A + 1) // 2
    for num in result:
        if result[num] > check:
            print('yes', num)
            break
    else:
        print('no')