# 2020.11.28
# 18:00 ~ 18:05

N = int(input())
lst = list(map(int, input().split()))
cnt = 0
last_num = lst[0]

for idx, num in enumerate(lst):
    if idx % 2 == num % 2:
        print("NO")
        break
else:
    print("YES")