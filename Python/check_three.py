N = int(input())
K = int(input())

def combi(n, c):
    def facto(num):
        res = 1
        for i in range(2, num + 1):
            res *= i
        return res
    return facto(n) // facto(c) // facto(n - c)

two = N // 2
one = N // 2 + N % 2

answer = 0
for my_one in range(0, min(K, one) + 1):
    my_two = K - my_one
    if my_two > two:
        continue
    if (my_one + my_two * 2) % 3 == 0:
        answer += combi(one, my_one) * combi(two, my_two)

print(answer)