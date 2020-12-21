def solution(k, score):
    res = {}
    cnts = {}
    last_score = score[0]
    for s in score[1:]:
        case = last_score - s
        if case in res:
            res[case].add(s)
            res[case].add(last_score)
            cnts[case] += 1
        else:
            res[case] = set()
            res[case].add(s)
            res[case].add(last_score)
            cnts[case] = 1
        last_score = s
    miss = set()
    for key in cnts:
        if cnts[key] >= k:
            miss = miss.union(res[key])
    answer = len(score) - len(miss)
    return answer

ex1 = 3, [24,22,20,10,5,3,2,1]

print(solution(*ex1))