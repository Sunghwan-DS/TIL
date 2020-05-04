R, C = map(int,input().split())
arr = [input() for _ in range(R)]
visited = [[-1] * C for _ in range(R)]

for i in range(R):
    visited[i][0] = i

for i in range(R):
    print(visited[i])
print()

for j in range(C-1):
    col_visited = {}
    for i in range(R):
        if visited[i][j] != -1:
            y = visited[i][j]
            for dy in (-1, 0, 1):
                ni = i + dy
                if 0 <= ni <= R-1 and arr[ni][j+1] == '.':
                    if visited[ni][j + 1] == -1:
                        if y not in col_visited:
                            col_visited[y] = 1
                            visited[ni][j + 1] = y
                            break
                        else:
                            visited[ni][j + 1] = y

for i in range(R):
    print(visited[i])
print()

ans_visited = [False] * R
ans = 0

for i in range(R):
    if visited[i][C-1] != -1:
        val = visited[i][C-1]
        if not ans_visited[val]:
            ans += 1
            ans_visited[val] = True

print(ans)