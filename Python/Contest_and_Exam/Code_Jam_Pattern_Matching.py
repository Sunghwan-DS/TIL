def revise_left(left, right, P):
    global end_case
    word = left+right
    length = min(len(word), len(P))
    for i in range(length):
        if P[i] != word[i]:
            end_case = True
            break
    else:
        if len(word) < len(P):
            return P
        else:
            return left


def revise_right(left, right, P):
    global end_case
    word = left+right
    length = min(len(word), len(P))
    for i in range(length):
        if P[len(P) - 1 - i] != word[len(word) - 1 - i]:
            end_case = True
            break
    else:
        if len(word) < len(P):
            return P
        else:
            return right


for tc in range(1, int(input())+1):
    N = int(input())
    left = ''
    right = ''
    end_case = False
    for _ in range(N):
        P = input()
        if P[0] == '*':
            P = P[1:]
            if not left+right:
                right = P
            else:
                right = revise_right(left, right, P)

        elif P[-1] == '*':
            P = P[:-1]
            if not left:
                left = P
            else:
                left = revise_left(left, right, P)

        else:
            P_L = ''
            P_R = ''
            LR = True
            for c in P:
                if c != '*':
                    if LR:
                        P_L += c
                    else:
                        P_R += c
                else:
                    LR = False
            if not left:
                left = P_L
            else:
                left = revise_left(left, right, P_L)

            if not right:
                right = P_R
            else:
                right = revise_right(left, right, P_R)

        if end_case:
            for ps in range(_+1, N):
                input()
            break

    if end_case:
        print("Case #%d: *"%(tc))
    else:
        length = min(len(left), len(right))
        R_idx = 0
        for L_idx in range(length, 0, -1):
            if left[len(left) - L_idx] == right[R_idx]:
                R_idx += 1
            else:
                R_idx = 0
                if left[len(left) - L_idx] == right[R_idx]:
                    R_idx += 1

        right = right[R_idx:]
        print("Case #%d:"%(tc), left + right)