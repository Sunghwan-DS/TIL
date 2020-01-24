table = [0] * 101
table[0] = 0
table[1] = 1
table[2] = 1
table[3] = 1

for i in range(4, 101):
    table[i] = table[i-2] + table[i-3]

n = int(input())
for i in range(n):
    k = int(input())
    print(table[k])