# 2020.11.28
# 18:35 ~ 18:46

N = int(input())
data = list(map(int, input().split()))

ans = 0
num = 1

for n in data:
    num *= n
    n %= (10 ** 9 + 7)
    ans += num
    num += 1

print(ans % (10 ** 9 + 7))