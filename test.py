N = int(input())
connect = [[] for _ in range(N+1)]
for i in range(N-1):
    a, b = map(int,input().split())
    connect[a].append(b)
    connect[b].append(a)

parent = [0] * (N+1)
parents = [1]
for i in connect[1]:
