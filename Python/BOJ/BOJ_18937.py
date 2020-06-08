N = int(input())
As = list(map(int, input().split()))
start = input()

kings = ('Blackking', 'Whiteking')
res = As[0] - 2
for num in As[1:]:
    res = res ^ (num - 2)

res = bin(res)[2:]
cnt = 0
for c in res:
    if c == '1':
        cnt += 1

if cnt % 2:
    print(start)
else:
    for king in kings:
        if king != start:
            print(king)
            break