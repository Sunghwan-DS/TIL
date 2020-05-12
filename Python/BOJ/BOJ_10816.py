N = int(input())
cards = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))

record = {}
for num in cards:
    if num not in record:
        record[num] = 1
    else:
        record[num] += 1

ans = []
for target in targets:
    if target in record:
        ans.append(record[target])
    else:
        ans.append(0)

print(*ans)