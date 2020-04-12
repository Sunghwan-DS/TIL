# class L_Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def append(self, data):
#         new = L_Node(data)
#         if self.head == None:
#             self.head = new
#             self.tail = new
#
#         else:
#             self.tail.next = new
#             self.tail = new
#
#
# class T_Node:
#     def __init__(self, data):
#         self.data = data
#         self.parent = None
#         self.child = LinkedList()
#         self.current = None
#
#
# class Tree:
#     def __init__(self):
#         self.root = None
#         self.current = None
#
#     def add(self, data):
#         new = T_Node(data)
#         if self.root == None:
#             self.root = new
#         else:
#             self.current.child.append(new)
#             new.parent = self.current


def DFS(current):
    visited[current] = True
    s = [current]
    DP[current][0] = population[current]
    while s:
        current = s[-1]
        for next in connection[current]:
            if not visited[next]:
                s.append(next)
                visited[next] = True
                DP[next][0] = population[next]
                break

        else:
            s.pop()
            if s:
                DP[s[-1]][0] += DP[current][1]
                DP[s[-1]][1] += max(DP[current][0], DP[current][1])


N = int(input())
population = [0] + list(map(int,input().split()))
connection = [[] for _ in range(N+1)]
for i in range(N-1):
    a, b = map(int,input().split())
    connection[a].append(b)
    connection[b].append(a)

DP = [[0, 0] for _ in range(N+1)]
visited = [False] * (N+1)
DFS(1)
print(max(DP[1][0], DP[1][1]))