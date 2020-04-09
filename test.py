class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node('head')
        self.tail = self.head
        self.current = self.head
        self.num_of_data = 0

    def append(self, data):
        new = Node(data)
        self.tail.next = new
        self.tail = new
        self.num_of_data += 1

    def insert(self, idx):
        left = 0
        self.current = self.head
        if idx != 0:
            for i in range(idx):
                self.current = self.current.next
            left = self.current.data

        if self.current.next != None:
            right = self.current.next.data
            new = Node(left + right)
            new.next = self.current.next
            self.current.next = new
        else:
            new = Node(left)
            self.current.next = new

    def print(self):
        self.current = self.head
        lst = []
        while self.current.next != None:
            self.current = self.current.next
            lst.append(self.current.data)

        return lst


for tc in range(1, int(input())+1):
    N, M, K = map(int,input().split())
    LList = LinkedList()
    data = list(map(int,input().split()))
    for num in data:
        LList.append(num)

    idx = 0
    for i in range(K):
        idx = (idx+M)%(LList.num_of_data)
        LList.insert(idx)

    print("#%d"%(tc), *LList.print())