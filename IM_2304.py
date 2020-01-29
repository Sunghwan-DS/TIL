N = int(input())
table = [0] * 1000
for _ in range(N):
    i, j = map(int,input().split())
    table[i-1] = j

height = max(table)
for _ in range(1000):
    if table[_] == height:
        idx1 = _
        break
for _ in range(999, -1, -1):
    if table[_] == height:
        idx2 = _
        break

result = 0
h = 0
for _ in range(idx1):
    if h < table[_]:
        h = table[_]
    result += h
h = 0
for _ in range(999, idx2, -1):
    if h < table[_]:
        h = table[_]
    result += h
for _ in range(idx1, idx2+1):
    result += height

print(result)