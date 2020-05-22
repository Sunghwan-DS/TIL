import random
import sys
# import time
# sys.stdin = open('in.txt','r')
input = sys.stdin.readline
# now = time.time()
def cal_cnt(random_color, A, B):
    low = 0
    high = len(record[random_color]) - 1

    # Lower_bound
    while low < high:
        m = (low + high) // 2
        if record[random_color][m] < A:
            low = m + 1
        else:
            high = m
    if record[random_color][high] < A:
        return 0
    else:
        start = high

    # upper_bound
    low = 0
    high = len(record[random_color])
    while low < high:
        m = (low + high) // 2
        if record[random_color][m] <= B:
            low = m + 1
        else:
            high = m
    high -= 1
    if record[random_color][high] > B:
        return 0
    else:
        end = high

    return end - start + 1


N, C = map(int, input().split())
caps = [0] + list(map(int, input().split()))
record = {}
for idx, color in enumerate(caps):
    if color not in record:
        record[color] = [idx]
    else:
        record[color].append(idx)

M = int(input())
visited = {}
for _ in range(M):
    A, B = map(int, input().split())
    check = (B - A + 1) // 2
    check_color = {}
    if A in visited:
        if B in visited[A]:
            print(visited[A][B])
            continue

    for _ in range(20):
        random_color = caps[random.randint(A, B)]
        if random_color in check_color:
            continue
        else:
            check_color[random_color] = 1
        cnt = cal_cnt(random_color, A, B)
        if cnt > check:
            print('yes', random_color)
            if A not in visited:
                visited[A] = {}
            visited[A][B] = 'yes ' + str(random_color)
            break
    else:
        print('no')
        if A not in visited:
            visited[A] = {}
        visited[A][B] = 'no'

# print('걸린 시간', time.time() - now)