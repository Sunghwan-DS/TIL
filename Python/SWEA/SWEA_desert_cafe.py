def check(y, x):
    global N, ans
    for a in range(1, x+1):
        for b in range(1, N-x):
            if y+a+b > N-1:
                continue

            ny = y
            nx = x
            TF = False
            lst = []

            for aa in range(a):
                ny += 1
                nx -= 1
                if arr[ny][nx] in lst:
                    TF = True
                    break
                else:
                    lst.append(arr[ny][nx])

            if TF:
                continue

            for bb in range(b):
                ny += 1
                nx += 1
                if arr[ny][nx] in lst:
                    TF = True
                    break
                else:
                    lst.append(arr[ny][nx])

            if TF:
                continue

            for aa in range(a):
                ny -= 1
                nx += 1
                if arr[ny][nx] in lst:
                    TF = True
                    break
                else:
                    lst.append(arr[ny][nx])

            if TF:
                continue

            for bb in range(b):
                ny -= 1
                nx -= 1
                if arr[ny][nx] in lst:
                    TF = True
                    break
                else:
                    lst.append(arr[ny][nx])

            if TF:
                continue

            res = len(lst)
            ans = max(ans, res)


T = int(input())
for case in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    ans = -1
    for i in range(N):
        for j in range(N):
            check(i, j)
    print("#%d" % (case), ans)