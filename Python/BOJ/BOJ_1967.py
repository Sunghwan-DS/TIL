from collections import deque

class Node:
    def __init__(self, num, val, parent = None):
        self.num = num
        self.val = val
        self.parent = parent
        self.children = []


class Tree:
    def __init__(self, N):
        self.root = Node(1, 0)
        self.current = None
        self.node_list = [0] * (N+1)
        self.node_list[1] = self.root


    def append(self, parent, num, val):
        now = self.node_list[parent]
        new = Node(num, val, now)
        now.children.append(new)
        self.node_list[num] = new


    def BFS(self, node, N):
        q = deque()
        q.append((node, 0))
        visited = [False] * (N+1)
        visited[node.num] = True
        max_length = 0
        ans = 0
        while q:
            data = q.popleft()
            self.current = data[0]
            if data[1] > max_length:
                max_length = data[1]
                ans = data[0]

            if self.current.parent and not visited[self.current.parent.num]:
                visited[self.current.parent.num] = True
                q.append((self.current.parent, data[1] + self.current.val))

            for child in self.current.children:
                if not visited[child.num]:
                    visited[child.num] = True
                    q.append((child, data[1] + child.val))

        self.current = ans
        return max_length


N = int(input())
tree = Tree(N)

for i in range(N-1):
    parent, child, val = map(int,input().split())
    tree.append(parent, child, val)

tree.BFS(tree.root, N)
print(tree.BFS(tree.current, N))