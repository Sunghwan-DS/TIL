def move(R, B, O):
    y_R = R[0]
    x_R = R[1]
    y_B = B[0]
    x_B = B[1]
    y_O = O[0]
    x_O = O[1]

    while arr[y_R][x_R] != ".":
        x_R += 1





N, M =map(int,input().split())
arr = [input() for _ in range(N)]

# print(arr)

for i in range(N):
    for j in range(M):
        if arr[i][j] == "R":
            y_R = i
            x_R = j
        if arr[i][j] == "B":
            y_B = i
            x_B = j
        if arr[i][j] == "O":
            y_O = i
            x_O = j

result = 0

move([y_R, x_R], [y_B, x_B], [y_O, x_O])