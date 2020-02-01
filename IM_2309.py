table = []
for _ in range(9):
    table.append(int(input()))
full = sum(table)
check = sum(table) - 100
TF = False
for idx, i in enumerate(table):
    if TF:
        True
    else:
        for j in table[idx+1:]:
            if i + j == check:
                table.remove(i)
                table.remove(j)
                TF = True
                break
table.sort()
for i in table:
    print(i)