import random

N, C = map(int, input().split())
caps = [0] + list(map(int, input().split()))
record = {}
for idx, color in enumerate(caps):
    if color not in record:
        record[color] = [idx]
    else:
        record[color].append(idx)

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

        cnt = 0
        for idx in record[random_color]:
            if idx > B:
                break
            elif idx >= A:
                cnt += 1
        if cnt > check:
            print('yes', random_color)
            break
    else:
        print('no')