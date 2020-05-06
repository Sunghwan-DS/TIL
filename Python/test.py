N = int(input())
sentence = list(input().split())
data = [0]
for word in sentence:
    data.append(len(word))

DP = [0] + [1000000] * (len(data)-1)
for cur in range(1, len(data)):
    for new in range(cur, 0, -1):
        new_list = data[new:cur+1]
        check = sum(new_list) + (len(new_list) - 1)
        if check <= N:
            DP[cur] = min(DP[new-1] + (N - check) ** 3, DP[cur])
        else:
            break

# print(data)
# print(DP)

print(DP[-1])