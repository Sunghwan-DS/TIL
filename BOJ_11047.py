N, K = map(int,input().split())
res = [0] * N
A = [0] * N
A[0] = int(input())
res[0] = K // A[0]

for i in range(1, N):
    A[i] = int(input())
    res[i] = res[i-1] // (A[i] // A[i-1])
    res[i-1] %= (A[i] // A[i-1])

print(sum(res))