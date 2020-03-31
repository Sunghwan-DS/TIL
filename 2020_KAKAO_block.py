board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]

def issafe(coordinate):
    global N
    if 0 <= coordinate <= N-1:
        return True
    else:
        return False


def solution(board):
    global N
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    answer = 0
    N = len(board[0])
    visited = [[[False, False] for _ in range(N)] for _ in range(N)]
    visited[0][0][1] = True
    q = [(0, 0, 0, 1, 1)]
    while q:
        answer += 1
        for _ in range(len(q)):
            y1, x1, y2, x2, dir = q.pop(0)

            for d in range(4):
                ny1 = y1 + dy[d]
                nx1 = x1 + dx[d]
                ny2 = y2 + dy[d]
                nx2 = x2 + dx[d]

                if issafe(ny1) and issafe(nx1) and issafe(ny2) and issafe(nx2) and board[ny1][nx1] == 0 and board[ny2][nx2] == 0:
                    if not visited[ny1][nx1][dir]:
                        visited[ny1][nx1][dir] = True
                        q.append((ny1, nx1, ny2, nx2, dir))
                        if ny2 == N-1 and nx2 == N-1:
                            return answer

                    if abs(dir - d)%2 == 1:
                        new_dir = (dir + 1) % 2
                        nny1 = y1
                        nnx1 = x1
                        nny2 = ny1
                        nnx2 = nx1
                        if nny1+nnx1 > nny2+nnx2:
                            nny1, nnx1, nny2, nnx2 = nny2, nnx2, nny1, nnx1
                        if not visited[nny1][nnx1][new_dir]:
                            visited[nny1][nnx1][new_dir] = True
                            q.append((nny1, nnx1, nny2, nnx2, new_dir))

                        nny1 = ny2
                        nnx1 = nx2
                        nny2 = y2
                        nnx2 = x2
                        if nny1+nnx1 > nny2+nnx2:
                            nny1, nnx1, nny2, nnx2 = nny2, nnx2, nny1, nnx1
                        if not visited[nny1][nnx1][new_dir]:
                            visited[nny1][nnx1][new_dir] = True
                            q.append((nny1, nnx1, nny2, nnx2, new_dir))

print(solution(board))