# # IM_5174
# def find_child(n):
#     global ans
#     if len(lst)-1 >= n*2:
#         if lst[n*2] != 0:
#             ans += 1
#             find_child(n*2)
#
#     if len(lst)-1 >= n*2 + 1:
#         if lst[n*2 + 1] != 0:
#             ans += 1
#             find_child(n*2 + 1)
#
#
# T = int(input())
# for case in range(1, T+1):
#     E, N = map(int,input().split())
#     data = list(map(int,input().split()))
#     lst = [0, data[0]]
#     for i in range(E):
#         p = data[2*i]
#         c = data[2*i+1]
#         if len(lst)-1 < lst.index(p)*2:
#             for _ in range(lst.index(p)*2 - (len(lst)-1)):
#                 lst.append(0)
#             lst[lst.index(p)*2] = c
#         else:
#             lst.append(0)
#             lst[-1] = c
#
#     n = lst.index(N)
#     ans = 1
#     find_child(n)
#     print("#%d"%(case), ans)


# # IM_5176
# def in_order_traverse(idx):
#     global cnt, N, ans
#     if idx*2 <= N:
#         in_order_traverse(idx * 2)
#     cnt += 1
#     if idx == N//2:
#         ans = cnt
#
#     if idx*2+1 <= N:
#         in_order_traverse(idx * 2 + 1)
#
#
# T = int(input())
# for case in range(1, T+1):
#     N = int(input())
#
#     lst = [0] * (N+1)
#     ans = 0
#     cnt = 0
#
#     if 2 <= N:
#         in_order_traverse(2)
#     cnt += 1
#     root = cnt
#
#     if 3 <= N:
#         in_order_traverse(3)
#
#     print("#%d"%(case), root, ans)


# # IM_5177
# def add_heap(num):
#     lst.append(num)
#     idx = len(lst) - 1
#     while True:
#         if lst[idx//2] < num:
#             return
#         else:
#             lst[idx//2], lst[idx] = lst[idx], lst[idx//2]
#             idx //= 2
#
# T = int(input())
# for case in range(1, T+1):
#     N = int(input())
#     data = list(map(int,input().split()))
#     lst = [0, data[0]]
#     for i in data[1:]:
#         add_heap(i)
#
#     ans = 0
#     idx = len(lst)-1
#     while True:
#         idx //= 2
#         if idx != 0:
#             ans += lst[idx]
#         else:
#             break
#
#     print("#%d"%(case), ans)


# IM_5178
def post_order_traverse(idx):
    global N
    if lst[idx] != 0:
        return lst[idx]

    if idx * 2 <= N:
        left = post_order_traverse(idx * 2)
    else:
        left = 0

    if idx*2+1 <= N:
        right = post_order_traverse(idx * 2 + 1)
    else:
        right = 0

    return left + right

T = int(input())
for case in range(1, T+1):
    N, M, L = map(int,input().split())
    lst = [0] * (N+1)
    for _ in range(M):
        idx, num = map(int,input().split())
        lst[idx] = num

    print("#%d"%(case), post_order_traverse(L))