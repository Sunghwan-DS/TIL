N = int(input())
sequence = list(map(int, input().split()))
count = [1]
for i in range(1, N):
    result = 0
    for j in range(i):
        if sequence[i] > sequence[j]:
            if result < count[j]:
                result = count[j]
    count.append(result+1)

print(max(count))