N = int(input())
dic = {}
for i in range(N):
    word = input()
    n = len(word) - 1
    for c in word:
        if c in dic:
            dic[c] += 10 ** n
        else:
            dic[c] = 10 ** n
        n -= 1

lst = []
for i in dic:
    lst.append(dic[i])
lst.sort(reverse=True)
ans = 0
n = 9
for i in lst:
    ans += i * n
    n -= 1
print(ans)