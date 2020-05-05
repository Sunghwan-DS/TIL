import sys
import time
start = time.time()

R, C = map(int,input().split())
arr = [input() for _ in range(R)]
visited = [[i] + [-1] * (C-1) for i in range(R)]

for j in range(1, C):
    col_visited = {}
    for i in range(R):
        if arr[i][j] == '.':
            for dy in (-1, 0, 1):
                ni = i + dy
                if 0 <= ni <= R-1 and visited[ni][j-1] != -1:
                    if not col_visited.get(visited[ni][j-1]):
                        col_visited[visited[ni][j-1]] = 1
                        visited[i][j] = visited[ni][j-1]
                        break
                    else:
                        visited[i][j] = visited[ni][j-1]

for i in range(R):
    print(visited[i])
print()
print(len(col_visited))
print("time :", time.time() - start)