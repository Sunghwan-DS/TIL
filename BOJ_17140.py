r, c, k = map(int,input().split())
arr = [list(map(int,input())) for _ in range(3)]
cnt = 0
x = 3
y = 3
while not arr[r-1][c-1] == k:
    cnt += 1
    if cnt > 100:
        print("-1")
        exit()

    if x >= y:
        