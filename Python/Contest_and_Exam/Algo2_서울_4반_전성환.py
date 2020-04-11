dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr =[list(map(int,input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    ans_area = 0
    ans = 0

    for i in range(N):
        for j in range(N):
            if not visited[i][j] and arr[i][j] > 0:
                s = [(i, j)]
                visited[i][j] = True
                cnt_area = 1
                res = arr[i][j]
                while s:
                    y, x = s.pop()
                    for dir in range(8):
                        ny = y + dy[dir]
                        nx = x + dx[dir]
                        if 0 <= ny <= N-1 and 0 <= nx <= N-1 and not visited[ny][nx] and arr[ny][nx] == arr[i][j]:
                            s.append((ny, nx))
                            visited[ny][nx] = True
                            cnt_area += 1
                            res += arr[i][j]
                if ans < res:
                    ans = res
                    ans_area = cnt_area
                elif ans == res:
                    ans_area = min(ans_area, cnt_area)

    print("#%d"%(tc), ans, ans_area)