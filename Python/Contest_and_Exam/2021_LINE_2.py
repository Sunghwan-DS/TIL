# 10:07 ~ 10:20

def solution(ball, order):
    request = {}
    front = 0
    back = len(ball) - 1

    answer = []

    for num in order:
        if num == ball[front]:
            front += 1
            answer += [num]
            if len(answer) == len(ball):
                break
            while ball[front] in request:
                del request[ball[front]]
                answer += [ball[front]]
                front += 1

        elif num == ball[back]:
            back -= 1
            answer += [num]
            if len(answer) == len(ball):
                break
            while ball[back] in request:
                del request[ball[back]]
                answer += [ball[back]]
                back -= 1

        else:
            request[num] = 1

    return answer


ex1 = ([1, 2, 3, 4, 5, 6], [6, 2, 5, 1, 4, 3]) # ans = [6, 5, 1, 2, 4, 3]
ex2 = ([11, 2, 9, 13, 24], [9, 2, 13, 24, 11]) # ans = [24, 13, 9, 2, 11]
ex3 = ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
ex4 = ([1, 2, 3, 4, 5], [4, 1, 2, 3, 5])

print(solution(*ex4))