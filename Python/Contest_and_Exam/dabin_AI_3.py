# 최대 금액 40
# 통장 갯수 12개


def solution(n, bankbook):
    res = dict()
    kind_of_money = []
    for money in bankbook:
        if money in res:
            res[money] += 1
        else:
            res[money] = 1
            kind_of_money.append(money)

    use = dict()
    for key in res:
        use[key] = 0

    kind_of_money.sort(reverse=True)
    answer = 0
    while True:
        money = 0
        for key in kind_of_money:
            while use[key] < res[key]:
                if money + key <= n:
                    use[key] += 1
                    money += key
                else:
                    break
            if money == n:
                break

        if money == 0:
            break
        else:
            answer += 1

    return answer

ex1 = 10, [8,4,2,5,3,7] # 3
ex2 = 10, [1,2,3,3,3,8] # 2
ex3 = 12, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] # 7
ex4 = 40, [30] # 1

print(solution(*ex4))