N = int(input())
sequence = list(map(int, input().split()))
count1 = [1]
for i in range(1, N):
    result = 0
    for j in range(i):
        if sequence[i] > sequence[j]:
            if result < count1[j]:
                result = count1[j]
    count1.append(result + 1)

sequence.reverse()

count2 = [1]
for i in range(1, N):
    result = 0
    for j in range(i):
        if sequence[i] > sequence[j]:
            if result < count2[j]:
                result = count2[j]
    count2.append(result + 1)
count2.reverse()
count = [count1[i] + count2[i] - 1 for i in range(N)]

print(max(count))