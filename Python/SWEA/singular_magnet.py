def rotation(num, LR):
    global a, b, c, d
    check = [0] * 3
    if magnet1[(a+2)%8] != magnet2[(b-2)%8]:
        check[0] = 1
    if magnet2[(b+2)%8] != magnet3[(c-2)%8]:
        check[1] = 1
    if magnet3[(c+2)%8] != magnet4[(d-2)%8]:
        check[2] = 1

    if num == 1:
        if LR == 1:
            a -= 1
            if check[0]:
                b += 1
                if check[1]:
                    c -= 1
                    if check[2]:
                        d += 1

        elif LR == -1:
            a += 1
            if check[0]:
                b -= 1
                if check[1]:
                    c += 1
                    if check[2]:
                        d -= 1

    elif num == 2:
        if LR == 1:
            b -= 1
            if check[0]:
                a += 1
            if check[1]:
                c += 1
                if check[2]:
                    d -= 1

        elif LR == -1:
            b += 1
            if check[0]:
                a -= 1
            if check[1]:
                c -= 1
                if check[2]:
                    d += 1

    elif num == 3:
        if LR == 1:
            c -= 1
            if check[2]:
                d += 1
            if check[1]:
                b += 1
                if check[0]:
                    a -= 1

        elif LR == -1:
            c += 1
            if check[2]:
                d -= 1
            if check[1]:
                b -= 1
                if check[0]:
                    a += 1

    elif num == 4:
        if LR == 1:
            d -= 1
            if check[2]:
                c += 1
                if check[1]:
                    b -= 1
                    if check[0]:
                        a += 1

        elif LR == -1:
            d += 1
            if check[2]:
                c -= 1
                if check[1]:
                    b += 1
                    if check[0]:
                        a -= 1


T = int(input())
for _ in range(T):
    K = int(input())
    magnet1 = list(map(int, input().split()))
    magnet2 = list(map(int, input().split()))
    magnet3 = list(map(int, input().split()))
    magnet4 = list(map(int, input().split()))

    a = 24
    b = 24
    c = 24
    d = 24

    for __ in range(K):
        num, LR = map(int, input().split())
        rotation(num, LR)

    print("#%d %d"%(_+1, magnet1[a%8] + magnet2[b%8] * 2 + magnet3[c%8] * 4 + magnet4[d%8] * 8))