class Node:
    def __init__(self, parent = None):
        self.parent = parent
        self.child = []



class Tree:
    def __init__(self):
        self.root = Node('root')
        self.current = self.root
        self.num_of_apple = 0
        self.val = 0

    def append(self):
        self.current.child.append(Node(self.current))
        self.current = self.current.child[-1]
        self.num_of_apple += 1
        self.val += 1



N = int(input())
data = input()
i, j = map(int,input().split())

apple_i = 0
apple_j = 0

tree = Tree()
for idx in range(len(data)):
    if data[idx] == '0':
        tree.append()
        if tree.num_of_apple == i:
            apple_i = tree.current

        if tree.num_of_apple == j:
            apple_j = tree.current

        if tree.current =
    else:
