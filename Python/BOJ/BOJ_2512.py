N = int(input())
budgets = list(map(int, input().split()))
total = int(input())

max_ans = max(budgets)
ans = total // N
while True:
    result = 0
    check = 0
    for budget in budgets:
        if budget > ans:
            check += 1
            result += ans
        else:
            result += budget

    if check > 0:
        revise = (total - result) // check
    else:
        break

    if revise > 0:
        ans += revise
    else:
        break

if ans >= max_ans:
    print(max_ans)
else:
    print(ans)