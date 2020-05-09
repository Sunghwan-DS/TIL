def solution(board):
    from collections import deque
    arr_y = len(board)
    arr_x = len(board[0])
    visited = [[625*500] * arr_x for _ in range(arr_y)]
    visited[0][0] = 0
    q = deque()
    q.append((0, 0, 0, 0))

    dy = (0, 1, 0, -1)
    dx = (1, 0, -1, 0)
    price = (100, 600, 400000, 600)

    while q:
        y, x, res, last_dirc = q.popleft()
        for dirc in range(4):
            ny = y + dy[dirc]
            nx = x + dx[dirc]
            if y == 0 and x == 0:
                new_res = 100
            else:
                new_res = res + price[abs(last_dirc - dirc)]

            if 0 <= ny < arr_y and 0 <= nx < arr_x and board[ny][nx] == 0 and new_res <= visited[ny][nx]:
                visited[ny][nx] = new_res
                q.append((ny, nx, new_res, dirc))


    answer = visited[arr_y - 1][arr_x - 1]
    return answer

print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))