def solution(n, m, p):
    if n < m or p == 1:
        return -1

    if p % 2 == 1:
        if n > m or p >= m:
            answer = ((n+m) - 1 + p - 2) // (p - 1) * 2 - 1
        else:
            answer = -1

    else:
        if n >= m+2 or p >= m:
            answer = ((n+m) - 1 + p - 2) // (p - 1) * 2 - 1
        elif n == m + 1:
            answer = (n+m + p - 2) // (p - 1) * 2 - 1
        else:
            answer = -1

    return answer



sample1 = [2, 2, 2] # 5
sample2 = [2, 2, 1] # -1
sample3 = [10, 9, 5]
print(solution(*sample2))