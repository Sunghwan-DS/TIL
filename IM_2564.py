w, h = map(int, input().split())
N = int(input())
table = []
for _ in range(N+1):
    coordinates = list(map(int,input().split()))
    if coordinates[0] == 1:
        table.append(2*w + h - coordinates[1])
    elif coordinates[0] == 2:
        table.append(coordinates[1])
    elif coordinates[0] == 3:
        table.append(2*w + h + coordinates[1])
    elif coordinates[0] == 4:
        table.append(w + h - coordinates[1])
result = 0

for l in table[:-1]:
    result += min(abs(l - table[-1]), 2*w + 2*h - abs(l - table[-1]))

print(result)