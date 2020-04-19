N, M = map(int, input().split())
card = list(map(int, input().split()))
card.sort()
a = 0
b = 1
c = 2

answer = card[a] + card[b] + card[c]


def factorial(num):
    if num==0:
        return 1
    else:
        result = 1
        for i in range(1, num + 1):
            result *= i
        return result

sum=0
for i in range(int(factorial(N) / factorial(N - 3) / factorial(3))):
    if answer == M:
        print(M)
        exit()
    else:
        if c == N - 1:
            if b == N - 2:
                if a == N - 3:
                    print(answer)
                    exit()
                else:
                    a += 1
                    b = a + 1
                    c = b + 1
            else:
                b += 1
                c = b + 1
        else:
            c += 1
        sum = card[a] + card[b] + card[c]
        if answer<sum<=M:
            answer=sum
print(answer)