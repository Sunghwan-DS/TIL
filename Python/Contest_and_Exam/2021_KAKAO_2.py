# 14:19 ~ 14:41

def solution(orders, course):
    from itertools import combinations
    result = {}
    for order in orders:
        for i in range(2, len(order) + 1):
            for c in combinations(order, i):
                c = list(c)
                c.sort()
                c = ''.join(c)
                if c in result:
                    result[c] += 1
                else:
                    result[c] = 1

    rank = [[] for _ in range(11)]
    for key in result:
        if not rank[len(key)]:
            if result[key] >= 2:
                rank[len(key)].append((-result[key], key))
        else:
            already = rank[len(key)][0][1]
            if result[key] == result[already]:
                rank[len(key)].append((-result[key], key))
            elif result[key] > result[already]:
                rank[len(key)] = [(-result[key], key)]

    lst = []
    for i in course:
        lst += rank[i]
    lst.sort(key=lambda x:x[1])
    answer = []
    for val, key in lst:
        answer.append(key)
    return answer

ex1 = (["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4])
ex2 = (["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5])
ex3 = (["XYZ", "XWY", "WXA"], [2,3,4])

print(solution(*ex3))