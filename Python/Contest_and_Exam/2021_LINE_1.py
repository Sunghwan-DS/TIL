# 10:00 ~ 10:05

def solution(boxes):
    result = {}
    for item1, item2 in boxes:
        if item1 in result:
            del result[item1]
        else:
            result[item1] = 1
        if item2 in result:
            del result[item2]
        else:
            result[item2] = 1
    cnt = 0
    for key in result:
        cnt += 1
    answer = cnt // 2
    return answer


ex1 = [[1, 2], [2, 1], [3, 3], [4, 5], [5, 6], [7, 8]]
ex2 = [[1, 2], [3, 4], [5, 6]]

print(solution(ex1))