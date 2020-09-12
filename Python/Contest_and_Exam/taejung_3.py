def solution(n, products):
    import heapq

    answer = 0
    remain = []

    for num, price, limit in products:
        if num <= n * limit:
            answer += price * num
        else:
            answer += price * limit * n
            remain_num = num - n * limit
            max_profit = min(limit, remain_num) * price
            heapq.heappush(remain, [-max_profit, max_profit, remain_num, price, limit])

    for i in range(n):
        if remain:
            idx, profit, num, price, limit = heapq.heappop(remain)
            answer += profit
            remain_num = num - limit

            if remain_num > 0:
                max_profit = min(limit, remain_num) * price
                heapq.heappush(remain, [-max_profit, max_profit, remain_num, price, limit])

    return answer





sample1 = [2, [[10, 3, 2], [15, 2, 5]]]
sample2 = [3, [[6, 5, 1], [11, 3, 2], [7, 10, 3]]] # [재고, 개당 가격, 일일 판매 수량]

print(solution(*sample1))