import time
import random

def lower_bound(lst, target):
    low = 0
    high = len(lst) - 1

    while low < high:
        m = (low + high) // 2
        if lst[m] < target:
            low = m + 1
        else:
            high = m
    if lst[high] < target:
        return 'no'
    return high

def upper_bound(lst, target):
    low = 0
    high = len(lst)

    while low < high:
        m = (low + high) // 2
        if lst[m] <= target:
            low = m + 1
        else:
            high = m
    high -= 1
    if lst[high] > target:
        return 'no'
    return high

now = time.time()
# lst = [i for i in range(1, 300001)]
# print('리스트 생성', time.time() - now)
# print(lower_bound(lst, 176251))
# print('lower_bound', time.time() - now)
# print(upper_bound(lst, 8))
# print('upper_bound', time.time() - now)

# for _ in range(20):
#     random_num = random.choice([i for i in range(1, 300001)])

for i in range(10000):
    print(random.randint(1, 2))
print(time.time() - now)