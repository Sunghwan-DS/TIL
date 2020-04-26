class Node:
    def __init__(self, num, val):
        self.num = num
        self.val = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = Node(1, 0)


    def append(self, parent, num, val):
        now = self.root
        stack = [now]

        while stack:
            now = stack.pop()
            print(now.num)
            if now.num == parent:
                if not now.left:
                    now.left = Node(num, val)
                else:
                    now.right = Node(num, val)
                return

            if now.right:
                stack.append(now.right)
            if now.left:
                stack.append(now.left)


    def PreOrder(self, now):
        print(now.num, end='')
        if now.left:
            self.PreOrder(now.left)
        if now.right:
            self.PreOrder(now.right)

    def InOrder(self, now):
        if now.left:
            self.InOrder(now.left)
        print(now.num, end='')
        if now.right:
            self.InOrder(now.right)

    def PostOrder(self, now):
        if now.left:
            self.PostOrder(now.left)
        if now.right:
            self.PostOrder(now.right)
        print(now.data, end='')

N = int(input())
tree = Tree()

for i in range(N-1):
    parent, child, val = map(int,input().split())
    tree.append(parent, child, val)

tree.InOrder(tree.root)