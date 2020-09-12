def solution(T,R,k):
    answer = 0
    condition = {}
    for S, E in R:
        if E not in condition:
            condition[E] = [S]
        else:
            condition[E].append(S)

    s = [(k, T[k-1])]
    while s:
        now, time = s.pop()
        answer = max(answer, time)
        if now in condition:
            for w in condition[now]:
                s.append((w, time + T[w-1]))

    return answer




my_T = [5, 8, 3, 7, 10, 5, 4]
my_R = [[1, 2], [2, 4], [1, 4], [6, 5], [3, 5], [4, 6]]
my_K = 5
# 1 => 2 => 4 => 6 => 5
#                3 => 5
print(solution(my_T, my_R, my_K))