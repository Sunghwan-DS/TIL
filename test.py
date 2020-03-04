def go(word, y, x):
    global ans
    if len(word) == 7:
        ans.add(word)
        return

    for dir in range(4):
        ny = y + dy[dir]
        nx = x + dx[dir]
        if 0 <= ny <= 3 and 0 <= nx <= 3:
            go(word+arr[ny][nx], ny, nx)

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for tc in range(1, int(input())+1):
    arr = [list(input().split()) for _ in range(4)]
    ans = set()
    for i in range(4):
        for j in range(4):
            go(arr[i][j], i, j)

    print("#%d"%(tc), len(ans))