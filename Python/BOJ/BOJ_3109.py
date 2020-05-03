R, C = map(int,input().split())
arr = [input() for _ in range(R)]
visited = [[True] * C] + [[False] * C for _ in range(R-1)]

for j in range(C-1):
    for i in range(R):
        if visited[i][j]:
            for dy in (-1, 0, 1):
                ni = i + dy
                if 0 <= ni <= R-1 and arr[ni][j+1] == '.' and not visited[ni][j+1]:
                    visited[ni][j] = True
                    break


