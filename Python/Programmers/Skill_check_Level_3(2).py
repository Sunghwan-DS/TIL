# 돌다리
from collections import deque

def solution(stones, k):
    stack = deque()
    for idx in range(k):
        stack.append(stones[idx])
    ans = max(stack)
    res = ans
    idx = k
    while idx < len(stones):
        if stones[idx] < ans:
            if stack[0] == res:
                stack.popleft()
                stack.append(stones[idx])
                res = max(stack)
                ans = min(ans, res)
            else:
                stack.popleft()
                stack.append(stones[idx])
            idx += 1
        else:
            if idx + k + 1 < len(stones):
                stack = deque()
                for i in range(idx+1, idx+k+1):
                    stack.append(stones[i])
                res = max(stack)
                idx += k + 1
            else:
                break
    return ans

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 10))