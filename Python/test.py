import sys
import time
start = time.time()

def BT(y, x):
    global C, cnt, isfound
    if x == C:
        cnt += 1
        isfound = True
        return
    dy = [-1, 0, 1]

    for i in range(3):
        ny = y + dy[i]
        if 0 <= ny < R and field[ny][x] == '.':
            field[ny][x] = 'x'
            BT(ny, x+1)
            if isfound: return


R, C = map(int, input().split())
field = [list(input()) for j in range(R)]
dy = [-1, 0, 1]
cnt = 0

for i in range(R):
    isfound = False
    BT(i, 1)

print(cnt)
print("time :", time.time() - start)