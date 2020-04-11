N, K = map(int,input().split())
field = [[0,0] for _ in range(6)]

for _ in range(N):
    s, grade = map(int,input().split())
    field[grade-1][s] += 1

result = 0
for i in field:
    for j in i:
        result += (j+K-1) // K

print(result)