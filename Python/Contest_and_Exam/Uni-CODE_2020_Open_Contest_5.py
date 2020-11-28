# 2020.11.28
# 18:46 ~ 19:18

# 최대 1000개의 지점, 2000개의 길, 100개의 마법,

from collections import deque

N, M, A, B = map(int, input().split())
road = {}
magic = []
row = []
for i in range(M):
    U, V, T = map(int, input().split())
    if U in road:
        road[U].add((V, i))
    else:
        road[U] = set()
        road[U].add((V, i))
    if V in road:
        road[V].add((U, i))
    else:
        road[V] = set()
        road[V].add((U, i))
    row.append(T)
magic.append(row)

K = int(input())
for _ in range(K):
    row = list(map(int, input().split()))
    magic.append(row)

res = [[10**13] * (K+1) for _ in range(N+1)]
q = deque()
q.append((A, 0))
res[A][0] = 0

while q:
    s, row = q.popleft()
    for tu in road[s]:
        e, i = tu
        new = res[s][row] + magic[row][i]
        if res[e][row] > new:
            res[e][row] = new
            q.append((e, row))
        if row < K:
            new = res[s][row] + magic[row + 1][i]
            if res[e][row + 1] > new:
                res[e][row + 1] = new
                q.append((e, row + 1))

print(min(res[B]))