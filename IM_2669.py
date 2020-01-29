field = [[0] * 100 for _ in range(100)]
for _ in range(4):
    data = list(map(int, input().split()))
    for i in range(data[1], data[3]):
        for j in range(data[0], data[2]):
            field[i][j] = 1

result = 0
for _ in range(100):
    result += sum(field[_])

print(result)