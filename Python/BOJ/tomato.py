M, N, H = map(int,input().split())
field = []
check = []
for _ in range(H):
    table = []
    for __ in range(N):
        a = list(map(int,input().split()))
        table.append(a)
        for idx, value in enumerate(a):
            if value == 1:
                check.append([_, __, idx])
    field.append(table)
if check == []:
    print("0")
    exit()
new_check = []
cnt = 0
while True:
    for H, i, j in check:
        if j-1 >= 0:
            if field[H][i][j - 1] == 0:
                field[H][i][j - 1] = 1
                new_check.append([H, i, j - 1])
        if j+1 <= M-1:        
            if field[H][i][j + 1] == 0:
                field[H][i][j + 1] = 1
                new_check.append([H, i, j + 1])
        if i-1 >= 0:
            if field[H][i - 1][j] == 0:
                field[H][i - 1][j] = 1
                new_check.append([H, i - 1, j])
        if i+1 <= N-1:
            if field[H][i + 1][j] == 0:
                field[H][i + 1][j] = 1
                new_check.append([H, i + 1, j])
        if H-1 >= 0:
            if field[H - 1][i][j] == 0:
                field[H - 1][i][j] = 1
                new_check.append([H - 1, i, j])
        if H+1 <= H-1:
            if field[H + 1][i][j] == 0:
                field[H + 1][i][j] = 1
                new_check.append([H + 1, i, j])
    
    if new_check == []:
        TFTF = False
        for H in range(H):
            for i in range(N):
                for j in range(M):
                    if field[H][i][j] == 0:
                        TFTF = True 
        break

    check = new_check[:]
    new_check = []
    cnt += 1

if TFTF:
    print("-1")

else:
    print(cnt)