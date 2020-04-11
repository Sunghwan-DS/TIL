for tc in range(1, int(input()) + 1):
    N, dir = input().split()
    N = int(N)
    arr = [list(map(int, input().split())) for _ in range(N)]

    if dir == 'up':
        for j in range(N):
            save = 1
            front = 0
            for i in range(N):
                if arr[i][j] != 0:
                    if arr[i][j] == save:
                        arr[front][j] = save*2
                    else:
                        arr[front][j] = save
                        save = arr[i][j]
                    front += 1
                    arr[i][j] = 0
            if save != 1:
                arr[front][j] = save


    elif dir == 'down':
        for j in range(N):
            save = 1
            front = N-1
            for i in range(N-1, -1, -1):
                if arr[i][j] != 0:
                    if arr[i][j] == save:
                        arr[front][j] = save*2
                    else:
                        arr[front][j] = save
                        save = arr[i][j]
                    front -= 1
                    arr[i][j] = 0
            if save != 1:
                arr[front][j] = save

    elif dir == 'left':
        for i in range(N):
            save = 1
            front = 0
            for j in range(N):
                if arr[i][j] != 0:
                    if arr[i][j] == save:
                        arr[i][front] = save*2
                    else:
                        arr[i][front] = save
                        save = arr[i][j]
                    front += 1
                    arr[i][j] = 0
            if save != 1:
                arr[i][front] = save

    elif dir == 'right':
        for i in range(N):
            save = 1
            front = N-1
            for j in range(N-1, -1, -1):
                if arr[i][j] != 0:
                    if arr[i][j] == save:
                        arr[i][front] = save*2
                    else:
                        arr[i][front] = save
                        save = arr[i][j]
                    front -= 1
                    arr[i][j] = 0
            if save != 1:
                arr[i][front] = save

    print("#%d"%(tc))
    for i in range(N):
        print(*arr[i])