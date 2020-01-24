n = int(input())

if n == 1:
    print(int(input()))
    exit()

table = [0] * n
table[0] = int(input())

for i in range(2, n+1):
    row = list(map(int, input().split()))
    for j in range(i-1, 0, -1):
        table[j] = max(table[j], table[j-1]) + row[j]
    table[0] += row[0]
print(max(table))