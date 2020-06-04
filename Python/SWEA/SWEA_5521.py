for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [{} for _ in range(N+1)]

    for _ in range(M):
        A, B = map(int, input().split())
        arr[A][B] = 1
        arr[B][A] = 1

    friends = {}
    invite = {}
    for i in range(2, N+1):
        if i in arr[1]:
            friends[i] = 1

    for friend in friends:
        for i in range(2, N+1):
            if i in arr[friend] and i not in friends:
                invite[i] = 1
    print("#%d"%(tc), len(friends) + len(invite))