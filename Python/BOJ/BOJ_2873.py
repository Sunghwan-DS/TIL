R, C = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(R)]

ans = ''
if R%2:
    for idx in range(R):
        if idx%2 == 0:
            ans += 'R' * (C-1)
            ans += 'D'
        else:
            ans += 'L' * (C-1)
            ans += 'D'
    ans = ans[:-1]
    print(ans)

elif C%2:
    for idx in range(C):
        if idx%2 == 0:
            ans += 'D' * (R-1)
            ans += 'R'
        else:
            ans += 'U' * (R-1)
            ans += 'R'
    ans = ans[:-1]
    print(ans)

else:
    low = 1000
    position = [-1, -1]
    for i in range(R):
        if i % 2 == 0:
            for j in range(1, C, 2):
                if low > arr[i][j]:
                    low = arr[i][j]
                    position = [i, j]
        else:
            for j in range(0, C, 2):
                if low > arr[i][j]:
                    low = arr[i][j]
                    position = [i, j]

    ans = ('D' * (R - 1) + 'R' + 'U' * (R - 1) + 'R') * (position[1] // 2)
    x = 2 * (position[1] // 2)
    y = 0
    xbound = 2 * (position[1] // 2) + 1
    while x != xbound or y != R - 1:
        if x < xbound and [y, xbound] != position:
            x += 1
            ans += 'R'
        elif x == xbound and [y, xbound - 1] != position:
            x -= 1
            ans += 'L'
        if y != R - 1:
            y += 1
            ans += 'D'

    ans += ('R' + 'U' * (R - 1) + 'R' + 'D' * (R - 1)) * ((C - position[1] - 1) // 2)
    print(ans)