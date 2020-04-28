from collections import deque

N = int(input())
Tree = [[0, [], 0] for _ in range(N+1)] # [[parent, child, val], ... , ]

for _ in range(N-1):
    parent, child, val = map(int,input().split())
    Tree[parent][1].append(child)
    Tree[child][0] = parent
    Tree[child][2] = val

q = deque()
q.append((1, 0))
visited = [False] * (N+1)
visited[1] = True

distance = 0
furthest = 0

while q:
    data = q.popleft()
    cur = data[0]
    res = data[1]

    if distance < res:
        distance = res
        furthest = cur

    parent = Tree[cur][0]
    children = Tree[cur][1]
    if parent and not visited[parent]:
        visited[parent] = True
        q.append((parent, res + cur[2]))

    for child in children:
        if not visited[child]:
            visited[child] = True
            q.append((child, res + Tree[child][2]))

distance = 0
q = deque()
q.append((furthest, 0))
visited = [False] * (N+1)
visited[furthest] = True
while q:
    data = q.popleft()
    cur = data[0]
    res = data[1]

    if distance < res:
        distance = res
        furthest = cur

    parent = Tree[cur][0]
    children = Tree[cur][1]
    if parent and not visited[parent]:
        visited[parent] = True
        q.append((parent, res + Tree[cur][2]))

    for child in children:
        if not visited[child]:
            visited[child] = True
            q.append((child, res + Tree[child][2]))

print(distance)