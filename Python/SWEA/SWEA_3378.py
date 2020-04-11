def check(c):
    global s, m, b
    if c == '(':
        s += 1
    elif c == ')':
        s -= 1
    elif c == '{':
        m += 1
    elif c == '}':
        m -= 1
    elif c == '[':
        b += 1
    elif c == ']':
        b -= 1


for tc in range(1, int(input()) + 1):
    p, q = map(int,input().split())
    s, m, b = 0, 0, 0
    result = []
    word = input()

    for i in word:
        check(i)

    for _ in range(p-1):
        word = input()
        last_s, last_m, last_b = s, m, b
        num_dot = 0
        TF = True
        for idx in range(len(word)):
            if word[idx] == '.':
                num_dot += 1
            else:
                save = idx
        for idx in range(save, len(word)):
            check(word[idx])
        result.append((last_s, last_m, last_b, num_dot))

    smb_list = []
    s, m, b = 0, 0, 0
    for _ in range(q-1):
        word = input()
        for i in word:
            check(i)
        smb_list.append((s, m, b))
    input()

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