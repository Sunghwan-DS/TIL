from itertools import combinations
lst = list(map(int,input().split()))
while True:
    for data in combinations(lst[1:], 6):
        print(*list(data))
    lst = list(map(int,input().split()))
    if len(lst) == 1:
        exit()
    print()