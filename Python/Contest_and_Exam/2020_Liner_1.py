def solution(inputString):
    answer = -1
    a, b, c, d = 0, 0, 0, 0
    res = 0
    for sym in inputString:
        if sym == '(':
            a += 1
            res += 1
        elif sym == ')':
            a -= 1
            if a < 0:
                return answer
        elif sym == '{':
            b += 1
            res += 1
        elif sym == '}':
            b -= 1
            if b < 0:
                return answer
        elif sym == '[':
            c += 1
            res += 1
        elif sym == ']':
            c -= 1
            if c < 0:
                return answer
        elif sym == '<':
            c += 1
            res += 1
        elif sym == '>':
            c -= 1
            if c < 0:
                return answer

    if a == 0 and b == 0 and c == 0 and d == 0:
        return res