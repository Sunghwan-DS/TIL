# 10:25 ~ 10:41

# 1000000000 이하, 최대 10자리
def solution(n):
    global min_cnt, val

    min_cnt = 1000000
    val = 0

    def cal_sum(num, cnt):
        global min_cnt, val
        if num < 10:
            if cnt < min_cnt:
                min_cnt = cnt
                val = num
            return

        divide = 10

        while True:
            a = num // divide
            b = num % divide
            if a < 1:
                return
            if divide == 10 and b == 0:
                cal_sum(a + b, cnt + 1)
            if b / divide >= 0.1:
                cal_sum(a + b, cnt + 1)
            divide *= 10

    cal_sum(n, 0)

    answer = [min_cnt, val]
    return answer


ex1 = 73425 # ans = [4, 3]
ex2 = 10007 # ans = [4, 8]
ex3 = 9 # ans = [0, 9]
ex4 = 1000 # ans = [3, 1]

print(solution(ex4))