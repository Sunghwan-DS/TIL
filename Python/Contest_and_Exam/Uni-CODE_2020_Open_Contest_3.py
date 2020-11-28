# 2020.11.28
# 18:13 ~ 18:35

N, K = map(int, input().split())
lst = list(map(int, input().split()))
data = []
for idx, cnt in enumerate(lst):
    data.append([cnt, str(idx + 1)])

data.sort(key=lambda x: -x[0])
if data[0][0] > N // 2 + N % 2:
    print("-1")
else:
    lst = []
    for cnt, num in data:
        lst += [num] * cnt
    end = len(lst)
    ans = []
    for i in range(end):
        if not i % 2:
            ans.append(lst[i // 2])
        else:
            ans.append(lst[end - 1 - i // 2])
    print(' '.join(ans))