class Node:
    def __init__(self, data, href):
        self.data = data
        self.href = href
        self.child = []
        self.parent = None


class Tree:
    def __init__(self):
        self.dummy = Node('dummy', None)
        self.current = self.dummy
        root = Node('/', '/')
        root.parent = self.dummy
        self.dummy.child.append(root)
        self.root = root


    def mkdir(self, href):
        self.current = self.dummy
        word = ''
        for c in href:
            word += c
            if c == '/':
                for idx in range(len(self.current.child)):
                    if self.current.child[idx].data == word:
                        self.current = self.current.child[idx]
                        word = ''
                        break
                else:
                    new_node = Node(word, href)
                    new_node.parent = self.current
                    self.current.child.append(new_node)
                    self.current = new_node


    def delete(self, href):
        self.current = self.dummy
        word = ''
        for c in href:
            word += c
            if c == '/':
                for idx in range(len(self.current.child)):
                    if self.current.child[idx].data == word:
                        self.current = self.current.child[idx]
                        word = ''
                        break
        delete_name = self.current.data
        self.current = self.current.parent
        for idx in range(len(self.current.child)):
            if self.current.child[idx].data == delete_name:
                self.current.child.pop(idx)
                break


    def list(self):
        self.current = self.dummy
        s = [self.current]
        while s:
            self.current = s.pop()
            for child in self.current.child:
                print(child.href)
                s.append(child)


tree = Tree()
tree.mkdir('/folder1/')
tree.mkdir('/folder2/')
tree.mkdir('/folder3/')
tree.mkdir('/folder2/folder4/')
print('삭제 전')
tree.list()
print('삭제 후')
tree.delete('/folder2/')
tree.list()