def check(i, j):
    queue = [i]
    checking = []
    cnt = 0
    table = [1]
    while queue:
        a = queue.pop(0)
        if field[a][j] == 1:
            break
        else:
            checking.append(a)
            for num, i in enumerate(field[a]):
                if i == 1 and num not in checking:
                    queue.append(num)
                    table.append(table[cnt]+1)
            cnt += 1
    return table[cnt]

N = int(input())
field = [[0] * (N+1) for _ in range(N+1)]
result = [[0] * (N+1) for _ in range(N+1)]

while True:
    a, b = map(int,input().split())
    if a == -1:
        break
    field[a][b] = 1
    field[b][a] = 1

# for _ in range(N+1):
#     print(field[_])
# print("필드")

score = [0] * (N+1)
score[0] = 100

for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j or result [i][j] != 0:
            pass
        else:
            value = check(i, j)
            result[i][j] = value
            result[j][i] = value
for i in range(1, N+1):
    score[i] = max(result[i])

# for _ in range(N+1):
#     print(result[_])
# print("결과")
#
# print(score)

cut = min(score)
lst = []
for idx, i in enumerate(score):
    if i == cut:
        lst.append(idx)

print(cut, len(lst))
print(" ".join([str(i) for i in lst]))