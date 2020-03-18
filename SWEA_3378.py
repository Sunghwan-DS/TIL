for tc in range(1, int(input()) + 1):
    p, q = map(int,input().split())
    s, m, b = 0, 0, 0
    smb_list = []
    result = []
    word = input()
    for i in word:
        if i == '(':
            s += 1
        elif i == ')':
            s -= 1
        elif i == '{':
            m += 1
        elif i == '}':
            m -= 1
        elif i == '[':
            b += 1
        elif i == ']':
            b -= 1

    for _ in range(p-1):
        word = input()
        num_dot = 0
        for i in word:
            if i == '.':
                num_dot += 1
            else:
                break
        result.append((s, m, b, num_dot))

        for i in word:
            if i == '(':
                s += 1
            elif i == ')':
                s -= 1
            elif i == '{':
                m += 1
            elif i == '}':
                m -= 1
            elif i == '[':
                b += 1
            elif i == ']':
                b -= 1

    smb_list = []
    s, m, b = 0, 0, 0
    for _ in range(q):
        word = input()
        for i in word:
            if i == '(':
                s += 1
            elif i == ')':
                s -= 1
            elif i == '{':
                m += 1
            elif i == '}':
                m -= 1
            elif i == '[':
                b += 1
            elif i == ']':
                b -= 1
        smb_list.append((s, m, b))
    smb_list.pop()

    possible = []
    for R in range(1, 21):
        for C in range(1, 21):
            for S in range(1, 21):
                for s, m, b, num_dot in result:
                    if R * s + C * m + S * b != num_dot:
                        break
                else:
                    possible.append((R, C, S))

    ans_list = [0]
    for s, m, b in smb_list:
        res = set()
        for R, C, S in possible:
            res.add(R * s + C * m + S * b)

        if len(res) == 1:
            res = list(res)
            ans_list.append(res[0])
        else:
            ans_list.append(-1)

    print("#%d"%(tc), *ans_list)