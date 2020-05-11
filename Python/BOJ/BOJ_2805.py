N, M = map(int, input().split())
trees = list(map(int, input().split()))

ans = 0
while True:
    res = 0
    check = 0
    for tree in trees:
        if tree > ans:
            res += tree - ans
            check += 1
    revise = (res - M) // check

    if revise > 0:
        ans += (res - M) // check
    else:
        break

print(ans)