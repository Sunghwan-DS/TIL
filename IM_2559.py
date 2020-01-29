N, K = map(int,input().split())
table = list(map(int,input().split()))

n = sum(table[0:K])
result = n
for i in range(K, N):
    n += table[i]
    n -= table[i-K]
    if n > result:
        result = n

print(result)