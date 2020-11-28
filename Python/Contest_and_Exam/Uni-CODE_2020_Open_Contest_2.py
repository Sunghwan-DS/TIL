# 2020.11.28
# 18:06 ~ 18:11

S = input()
num_of_zero = 0
for c in S:
    if c == '0':
        num_of_zero += 1
num_of_one = (len(S) - num_of_zero) // 2
num_of_zero //= 2

ans = ''
for c in S:
    if c == '0':
        if num_of_zero > 0:
            num_of_zero -= 1
            ans += '0'
    elif c == '1':
        if not num_of_one:
            ans += '1'
        else:
            num_of_one -= 1

print(ans)