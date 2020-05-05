N, K = map(int,input().split())
sequence = list(map(int,input().split()))
arr = [0] * (K + 1)
ans = 0
slot = 0
for num in sequence:
    if not arr[num]:
        slot += 1
        if slot - arr[num] > N:
            ans += 1
        arr[num] = slot

    elif slot - arr[num] >= N:
        ans += 1
        slot += 1
        arr[num] = slot

    print(arr, ans)


print(ans)


