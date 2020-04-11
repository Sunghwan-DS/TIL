# 2020.03.02
# 13:42 ~ 13:56
# BFS 구현
# 실행시간:260ms, 코드길이:834B

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

T = int(input())
for case in range(1, T+1):
    N, M, R, C, L = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    road = [(), (0, 1, 2, 3), (0, 2), (1, 3), (0, 1), (1, 2), (2, 3), (0, 3)]
    ans = 1
    q = [(R, C)]
    visited[R][C] = True
    for _ in range(L-1):
        for __ in range(len(q)):
            y, x = q.pop(0)

            for dir in range(4):
                ny = y + dy[dir]
                nx = x + dx[dir]

                if 0 <= ny <= N-1 and 0 <= nx <= M-1 and not visited[ny][nx] and dir in road[arr[y][x]] and (dir+2)%4 in road[arr[ny][nx]]:
                    q.append((ny, nx))
                    visited[ny][nx] = True
                    ans += 1

    print("#%d"%(case), ans)