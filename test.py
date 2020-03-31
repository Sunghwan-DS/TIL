board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]

def solution(board):
    answer = 0
    N = len(board[0])
    visited = [[False, False] for _ in range(N) for _ in range(N)]
    print(visited)


    return answer


print(solution(board))