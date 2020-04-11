class L_Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new = L_Node(data)
        if self.head == None:
            self.head = new
            self.tail = new

        else:
            self.tail.next = new
            self.tail = new


class T_Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.child = LinkedList()
        self.current = None


class Tree:
    def __init__(self):
        self.root = None
        self.current = None

    def add(self, data):
        new = T_Node(data)
        if self.root == None:
            self.root = new
        else:
            self.current.child.append(new)
            new.parent = self.current

N = int(input())
population = [0] + list(map(int,input().split()))
connection = [[] for _ in range(N+1)]
for i in range(N-1):
    a, b = map(int,input().split())
    connection[a].append(b)
    connection[b].append(a)


tree = Tree()
tree.add(1)

for child in connection[1]:
    if child !=
