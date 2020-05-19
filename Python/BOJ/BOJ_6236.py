# import sys
# sys.setrecursionlimit(10**6)
#
# def check(min_val, max_val):
#     global ans, M
#     K = (min_val + max_val) // 2
#     money = K
#     cnt = 1
#
#     for use in plan:
#         if money >= use:
#             money -= use
#         elif use > K:
#             check(K+1, max_val)
#             return
#         else:
#             cnt += 1
#             money = K - use
#
#     if cnt <= M:
#         ans = min(ans, K)
#         if min_val == max_val:
#             return
#         if min_val <= K-1:
#             check(min_val, K-1)
#     elif min_val == max_val:
#         return
#     elif K+1 <= max_val:
#         check(K+1, max_val)
#     return
#
#
# N, M = map(int, input().split())
# plan = []
# for _ in range(N):
#     plan.append(int(input()))
#
# ans = 500000001
# check(1, 500000000)
# print(ans)



N, M = map(int, input().split())
plan = []
for _ in range(N):
    plan.append(int(input()))

min_val = 1
max_val = 1000000000
ans = 1000000001

while min_val <= max_val:
    K = (min_val + max_val) // 2
    money = K
    cnt = 1

    for use in plan:
        if money >= use:
            money -= use
        elif use > K:
            min_val = K + 1
            cnt = M + 1
            break
        else:
            cnt += 1
            money = K - use

    if cnt <= M:
        ans = min(ans, K)
        max_val = K - 1
    else:
        min_val = K + 1

print(ans)