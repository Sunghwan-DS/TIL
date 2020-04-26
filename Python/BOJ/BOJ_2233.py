N = int(input())
data = 'X' + input()
i, j = map(int,input().split())
cnt = 0
stack = []
record = [[0] * (N+1) for _ in range(2001)]
for idx in range(1, len(data)):
    if data[idx] == '0':
        cnt += 1
        record[0][cnt] = idx
        stack.append(cnt)
        if idx == i:
            stack_i = stack[:]
        if idx == j:
            stack_j = stack[:]
    else:
        if idx == i:
            stack_i = stack[:]
        if idx == j:
            stack_j = stack[:]
        record[1][stack.pop()] = idx

for idx in range(min(len(stack_i), len(stack_j))):
    if stack_i[idx] != stack_j[idx]:
        idx -= 1
        break

print(record[0][stack_i[idx]], record[1][stack_i[idx]])