N = int(input())
connect = [[] for _ in range(N+1)]
for i in range(N-1):
    a, b = map(int,input().split())
    connect[a].append(b)
    connect[b].append(a)

parent = [0] * (N+1)
s = [1]
while s:
    p = s.pop()
    for i in connect[p]:
        if not parent[i]:
            parent[i] = p
            s.append(i)

for i in range(2, N+1):
    print(parent[i])