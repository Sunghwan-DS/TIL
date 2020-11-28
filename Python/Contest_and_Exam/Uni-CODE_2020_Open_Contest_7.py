# 2020.11.28
# 20:00 ~ 20:28

# 최대 컵 30만개, 동작 30만개, 쿼리 30만개

class Node:
    def __init__(self, K):


class SegmentTree:
    def make(self, actions, N, K):
        def bunhal(left, right):
            if left == right:




K, N, M = map(int, input().split())
actions = []
for _ in range(N-1):
    action = list(map(int, input().split()))
    actions.append(action)

query = []
for _ in range(M):
    s, m, t, a, b = map(int, input().split())
    cal(1, m - 1)
    cal(m, N-1)
    print(s)