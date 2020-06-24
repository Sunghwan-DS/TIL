def solution(prices):
    # answer = [0] * len(prices)
    # end = len(prices) - 1
    # record = {}
    # record[prices[-1]] = end
    # for idx in range(len(prices)-2, -1, -1):
    #     min_idx = 10000
    #     for key in record:
    #         if key < prices[idx]:
    #             min_idx = min(min_idx, record[key])
    #
    #     if min_idx == 10000:
    #         answer[idx] = end - idx
    #     else:
    #         answer[idx] = min_idx - idx
    #     record[prices[idx]] = idx

    # answer = [0] * len(prices)
    # record = [[] for _ in range(10001)]
    # last_val = 0
    # for idx, val in enumerate(prices):
    #     record[val].append(idx)
    #     if last_val > val:
    #         for v in range(val + 1, last_val + 1):
    #             for i in record[v]:
    #                 answer[i] = idx - i
    #             record[v] = []
    #     last_val = val
    #
    # end = len(prices) - 1
    # for v in range(1, 10001):
    #     for i in record[v]:
    #         answer[i] = end - i
    # return answer


    answer = [0] * len(prices)

    for i in range(len(prices) - 1):
        for j in range(i, len(prices) - 1):
            if prices[i] > prices[j]:
                break
            else:
                answer[i] += 1
    return answer

print(solution([1,2,3,2,3]))