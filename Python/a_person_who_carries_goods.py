T = int(input())

for _ in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    W = list(map(int, input().split()))
    A.sort(reverse = True)

    count = [0] * N
    move = True
    for __ in W:
        if __ > A[0]:
            print("#%d -1" % (_))
            move = False
            break

        for idx in range(N-1, -1, -1):
            if __ <= A[idx]:
                count[idx] += 1
                break

    if not move:
        continue

    time = min(count)

    if time != 0:
        for idx in range(N):
            count[idx] -= time

    while True:
        worked = False
        for idx in range(N):
            if count[idx] > 0:
                count[idx] -= 1
                worked = True
            elif count[idx] == 0:
                for sidx in range(idx + 1, N):
                    if count[sidx] > 0:
                        count[sidx] -= 1
                        worked = True
                        break
        if worked:
            time += 1
        else:
            break

    print("#%d %d"%(_, time))