# class Node:
#     def __init__(self, data=None):
#         self.data = data
#         self.next = [None] * 10
#
#
# class Trie:
#     def __init__(self):
#         self.head = Node('head')
#         self.current = self.head
#
#
# for tc in range(int(input())):
#     N = int(input())
#     trie = Trie()
#     for _ in range(N):
#         number = input()
#         trie.current = trie.head
#         stop = False
#         for string in number:
#             num = int(string)
#             if trie.current.next[num]:
#                 trie.current = trie.current.next[num]
#                 if trie.current.data:
#                     print('NO')
#                     stop = True
#                     break
#             else:
#                 trie.current.next[num] = Node()
#                 trie.current = trie.current.next[num]
#         trie.current.data = int(number)
#
#         if stop:
#             break
#
#     if not stop:
#         print('YES')


for tc in range(int(input())):
    N = int(input())
    numbers = {}
    stop = False
    for _ in range(N):
        number = input()
        for length in range(1, len(number)):
            string = number[:length]
            if string in numbers and numbers[string] == 2:
                print('NO')
                stop = True
                break
            else:
                numbers[string] = 1
        if stop:
            break

        if number in numbers:
            print('NO')
            stop = True
            break
        else:
            numbers[number] = 2
    else:
        print('YES')