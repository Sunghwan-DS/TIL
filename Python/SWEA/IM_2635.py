N = int(input())
result = 0
for i in range(1, N+1):
    table = [N]
    table.append(i)
    t = N - i
    while t >= 0:
        table.append(t)
        t = table[-2] - table[-1]

    if result < len(table):
        result_table = table
        result = len(table)

print(result)
print(" ".join([str(i) for i in result_table]))