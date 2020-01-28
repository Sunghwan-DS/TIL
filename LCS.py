word1 = input()
word2 = input()
result2 = [0] * (len(word1)+1)
result1 = result2[:]
for i in word2:
    for idx, j in enumerate(word1):
        if i == j:
            result2[idx + 1] = result1[idx] + 1
        else:
            result2[idx + 1] = max(result2[idx], result1[idx + 1])
    result1 = result2[:]

print(max(result2))