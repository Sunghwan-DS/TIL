def rot(idx, dir):
    rot_TF = [False] * 4
    rot_TF[idx-1] = True

    for i in range(idx-1, 3):
        if mag[i][2] == mag[i+1][-2]:
            break
        else:
            rot_TF[i+1] = True

    for i in range(idx-1, 0, -1):
        if mag[i][-2] == mag[i-1][2]:
            break
        else:
            rot_TF[i-1] = True

    d = [0] * 4
    for i in range(4):
        if (i-idx-1) % 2 == 0:
            d[i] = dir
        else:
            d[i] = -dir

    for i in range(4):
        if rot_TF[i]:
            if d[i] == 1:
                a = mag[i].pop()
                mag[i].insert(0, a)

            else:
                a = mag[i].pop(0)
                mag[i].append(a)


T = int(input())
for case in range(1, T+1):
    K = int(input())
    mag = []

    for _ in range(4):
        mag.append(list(map(int,input().split())))

    for _ in range(K):
        idx, dir = map(int,input().split())
        rot(idx, dir)

    ans = 0
    for i in range(4):
        if mag[i][0] == 1:
            ans += 2 ** i

    print("#%d"%(case), ans)