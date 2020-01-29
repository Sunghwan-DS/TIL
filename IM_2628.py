M, N = map(int,input().split())
cut = int(input())
table_y = [True] * N
table_y[-1] = False
table_x = [True] * M
table_x[-1] = False
for _ in range(cut):
    direction, idx = map(int,input().split())
    if direction == 0:
        table_y[idx-1] = False
    elif direction == 1:
        table_x[idx-1] = False

max_y = 0
max_x = 0
cnt = 0
for y in table_y:
    cnt += 1
    if y:
        pass
    else:
        if cnt > max_y:
            max_y = cnt
        cnt = 0

for x in table_x:
    cnt += 1
    if x:
        pass
    else:
        if cnt > max_x:
            max_x = cnt
        cnt = 0

print(max_y * max_x)