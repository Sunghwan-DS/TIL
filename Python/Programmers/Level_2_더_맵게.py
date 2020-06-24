# def solution(scoville, K):
#     if sum(scoville) < K:
#         return -1
#
#     scoville.sort()
#     scoville.insert(0, 0)
#     answer = 0
#     print("초기조건:", scoville)
#
#     while scoville[1] < K:
#         scoville[1], scoville[-1] = scoville[-1], scoville[1]
#         min_s = scoville.pop(-1)
#         target_idx = 1
#
#
#         # scoville[-1] = scoville[-1] * 2 + min_s
#         # target_idx = len(scoville) - 1
#         while True:
#             if scoville[target_idx] > scoville[target_idx * 2] or scoville[target_idx] > scoville[target_idx * 2 + 1]:
#                 if scoville[target_idx * 2] >= scoville[target_idx * 2 + 1]:
#                     scoville[target_idx], scoville[target_idx * 2 + 1] = scoville[target_idx * 2 + 1], scoville[target_idx]
#                     target_idx = target_idx * 2 + 1
#                 else:
#                     scoville[target_idx], scoville[target_idx * 2] = scoville[target_idx * 2], scoville[target_idx]
#                     target_idx *= 2
#             else:
#                 break
#         answer += 1
#         print(scoville)
#     return answer

import heapq

def solution(scoville, K):
    if sum(scoville) < K:
        return -1
    answer = 0
    scoville.sort()
    print(scoville)
    while scoville[0] < K:
        min_s = heapq.heappop(scoville)
        min2_s = heapq.heappop(scoville)
        heapq.heappush(scoville, min_s + min2_s * 2)
        answer += 1
        print(scoville)
    return answer


print(solution([1, 3], 7))