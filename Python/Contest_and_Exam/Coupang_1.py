def solution(N):
    answer = []
    max_val = 0
    for devide in range(2, 10):
        new = ''
        cnt = 0
        while N >= devide ** cnt:
            remain = (N % (devide ** (cnt + 1))) // devide ** cnt
            new = str(remain) + new
            cnt +=1

        res = 1
        for s in new:
            res *= int(s)
        if res >= max_val:
            answer = [devide, res]
            max_val = res
    return answer

print(solution(14))