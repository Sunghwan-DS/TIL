import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(cur, res):
    global max_fruits, max_location, min_node, N
    if max_fruits < res:
        max_fruits = res
        max_location = cur
        for num in range(1, N+1):
            if num in visited:
                break
        min_node = num

    elif max_fruits == res:
        for num in range(1, N+1):
            if num in visited:
                break
        min_node = min(min_node, num)

    for num in Tree[cur]:
        if num not in visited:
            visited[num] = 1
            DFS(num, res + fruits[num])
            del visited[num]


N = int(input())
fruits = [0] + list(map(int, input().split()))

Tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    A, B = map(int, input().split())
    Tree[A].append(B)
    Tree[B].append(A)

for num in range(1, N+1):
    Tree[num].sort()

visited = {}
visited[1] = 1
max_fruits = 0
max_location = 0
min_node = 0
DFS(1, fruits[1])

visited = {}
visited[max_location] = 1
max_fruits = 0
DFS(max_location, fruits[max_location])
print(max_fruits, min_node)