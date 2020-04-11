# # IM_5110
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class LinkedList:
#     def __init__(self):
#         dummy = Node("dummy")
#         self.head = dummy
#         self.tail = dummy
#
#         self.current = None
#         self.before = None
#
#         self.num_of_data = 0
#
#
#     def append(self, data):
#         new_node = Node(data)
#         self.tail.next = new_node
#         self.tail = new_node
#
#         self.num_of_data += 1
#
#
#     def first(self):
#         if self.num_of_data == 0:
#             return None
#
#         self.before = self.head
#         self.current = self.head.next
#
#         return self.current.data
#
#
#     def next(self):
#         if self.current.next == None:
#             return None
#
#         self.before = self.current
#         self.current = self.current.next
#
#         return self.current.data
#
# T = int(input())
# for case in range(1, T+1):
#     N, M = map(int,input().split())
#     LList = LinkedList()
#     seq = list(map(int,input().split()))
#
#     for i in seq:
#         LList.append(i)
#
#     for i in range(M-1):
#         seq = list(map(int,input().split()))
#         head = seq[0]
#         LList.first()
#         while LList.current.data <= head:
#             if LList.current is LList.tail:
#                 break
#             LList.next()
#
#         if LList.current is LList.tail and LList.current.data <= head :
#             for j in seq:
#                 LList.append(j)
#
#
#         else:
#             connection_node = LList.current
#             LList.current = LList.before
#             for j in seq:
#                 new_node = Node(j)
#                 LList.current.next = new_node
#                 LList.next()
#                 LList.num_of_data += 1
#             LList.current.next = connection_node
#
#     LList.first()
#     ans = [LList.current.data]
#     for i in range(LList.num_of_data - 1):
#         LList.next()
#         ans.append(LList.current.data)
#     ans.reverse()
#
#     if LList.num_of_data <= 10:
#         print("#%d"%(case), *ans)
#     else:
#         print("#%d"%(case), *ans[:10])