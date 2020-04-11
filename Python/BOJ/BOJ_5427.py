# 2020.03.24
# 12:58 ~ 13:35
# BFS 구현
#

import sys
from collections import deque


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for tc in range(1, int(sys.stdin.readline()) + 1):
    w, h = map(int,sys.stdin.readline().split())
    arr = [(sys.stdin.readline()) for _ in range(h)]
    fire_visited = [[False] * w for _ in range(h)]
    dog_visited = [[False] * w for _ in range(h)]

    fire = deque()
    dog = deque()

    for i in range(h):
        for j in range(w):
            if arr[i][j] == '*':
                fire.append((i, j))
                fire_visited[i][j] = True
            elif arr[i][j] == '@':
                dog.append((i, j))
                dog_visited[i][j] = True

    escape = False
    ans = 0
    while dog:
        ans += 1

        for i in range(len(fire)):
            y, x = fire.popleft()

            for dir in range(4):
                ny = y + dy[dir]
                nx = x + dx[dir]

                if 0 <= ny <= h-1 and 0 <= nx <= w-1 and not fire_visited[ny][nx] and arr[ny][nx] != '#':
                    fire_visited[ny][nx] = True
                    fire.append((ny, nx))

        for i in range(len(dog)):
            y, x = dog.popleft()

            for dir in range(4):
                ny = y + dy[dir]
                nx = x + dx[dir]

                if 0 <= ny <= h-1 and 0 <= nx <= w-1:
                    if not fire_visited[ny][nx] and not dog_visited[ny][nx] and arr[ny][nx] != '#':
                        dog_visited[ny][nx] = True
                        dog.append((ny, nx))

                else:
                    escape = True
                    break
            if escape:
                break
        if escape:
            break
    if escape:
        print(ans)
    else:
        print("IMPOSSIBLE")