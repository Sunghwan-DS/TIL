# 16:12 ~ 17:23

def solution(board, r, c):
    from collections import deque
    q = deque()
    q.append((r, c, 0, -1))

    dy = (0, -1, 0, 1)
    dx = (1, 0, -1, 0)
    need = 0
    for i in range(4):
        for j in range(4):
            if board[i][j]:
                need += 1

    def BFS(q):
        cnt = -1
        while True:
            cnt += 1
            cen = len(q)
            for _ in range(cen):
                r, c, score, choose = q.popleft()
                if score == need:
                    return cnt

                if board[r][c]:
                    if choose == -1:
                        choose = board[r][c]
                        board[r][c] = 0
                        q = deque()
                        q.append((r, c, score + 1, choose))
                        break

                    elif choose == board[r][c]:
                        board[r][c] = 0
                        q = deque()
                        q.append((r, c, score+1, -1))
                        break

                for i in range(4):
                    ny = r + dy[i]
                    nx = c + dx[i]
                    if 0 <= ny <= 3 and 0 <= nx <= 3:
                        q.append((ny, nx, score, choose))

                        while 0 <= ny <= 3 and 0 <= nx <= 3:
                            ny += dy[i]
                            nx += dx[i]
                            if 0 <= ny <= 3 and 0 <= nx <= 3:
                                if board[ny][nx]:
                                    q.append((ny, nx, score, choose))
                                    break

                        if not (0 <= ny <= 3 and 0 <= nx <= 3):
                            ny -= dy[i]
                            nx -= dx[i]
                            q.append((ny, nx, score, choose))

    answer = BFS(q)
    return answer


ex1 = ([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0) # 14
ex2 = ([[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]], 0, 1) # 16

print(solution(*ex2))