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
    for h, i, j in check:
        if j-1 >= 0:
            if field[h][i][j-1] == 0:
                field[h][i][j-1] = 1
                new_check.append([h, i, j-1])
        if j+1 <= M-1:        
            if field[h][i][j+1] == 0:
                field[h][i][j+1] = 1
                new_check.append([h, i, j+1])
        if i-1 >= 0:
            if field[h][i-1][j] == 0:
                field[h][i-1][j] = 1
                new_check.append([h, i-1, j])
        if i+1 <= N-1:
            if field[h][i+1][j] == 0:
                field[h][i+1][j] = 1
                new_check.append([h, i+1, j])
        if h-1 >= 0:
            if field[h-1][i][j] == 0:
                field[h-1][i][j] = 1
                new_check.append([h-1, i, j])
        if h+1 <= H-1: 
            if field[h+1][i][j] == 0:
                field[h+1][i][j] = 1
                new_check.append([h+1, i, j])
    
    if new_check == []:
        TFTF = False
        for h in range(H):
            for i in range(N):
                for j in range(M):
                    if field[h][i][j] == 0:
                        TFTF = True 
        break

    check = new_check[:]
    new_check = []
    cnt += 1

if TFTF:
    print("-1")

else:
    print(cnt)