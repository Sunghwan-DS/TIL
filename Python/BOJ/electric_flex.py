N = int(input())
pole1 = [0] * N
pole2 = [0] * N
table = []
sequence = [0] * N
for _ in range(N):
    table.append(list(map(int, input().split())))

table.sort()

for _ in range(N):
    sequence[_] = table[_][1]

count = [1]
for i in range(1, N):
    result = 0
    for j in range(i):
        if sequence[i] > sequence[j]:
            if result < count[j]:
                result = count[j]
    count.append(result+1)

print(N - max(count))