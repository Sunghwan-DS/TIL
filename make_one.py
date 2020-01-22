N = int(input())
cnt = 0

table = [0] * (N+1)

for i in range(2, N+1):
    if i % 6 == 0:
        table[i] = min(table[i//2], table[i//3], table[i-1]) + 1
        continue

    if i % 3 == 0:
        table[i] = min(table[i // 3], table[i - 1]) + 1
        continue

    if i % 2 == 0:
        table[i] = min(table[i // 2], table[i - 1]) + 1
        continue

    table[i] = table[i-1] + 1

print(table[N])