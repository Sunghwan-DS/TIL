def solution(numbers, hand):
    dy = (-1, 0, 1, 0)
    dx = (0, 1, 0, -1)

    def BFS(y, x, val):
        visited = [[False] * 3 for _ in range(4)]
        visited[y][x] = True
        if arr[y][x] == val:
            return 0

        cnt = 0
        q = [(y, x)]
        while q:
            cnt += 1
            for _ in range(len(q)):
                y, x = q.pop(0)
                for dirc in range(4):
                    ny = y + dy[dirc]
                    nx = x + dx[dirc]
                    if 0 <= ny <= 3 and 0 <= nx <= 2 and not visited[ny][nx]:
                        if arr[ny][nx] == val:
                            return cnt
                        else:
                            visited[ny][nx] = True
                            q.append((ny, nx))

    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [11, 0, 12]]
    location = ((3,1), (0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2))
    left = [3, 0]
    right = [3, 2]
    answer = ''

    for number in numbers:
        if number in (1, 4, 7):
            answer += 'L'
            left[0] = location[number][0]
            left[1] = location[number][1]
        elif number in (3, 6, 9):
            answer += 'R'
            right[0] = location[number][0]
            right[1] = location[number][1]
        else:
            cnt_left = BFS(left[0], left[1], number)
            cnt_right = BFS(right[0], right[1], number)
            if hand == "left":
                if cnt_left <= cnt_right:
                    answer += 'L'
                    left[0] = location[number][0]
                    left[1] = location[number][1]
                else:
                    answer += 'R'
                    right[0] = location[number][0]
                    right[1] = location[number][1]
            else:
                if cnt_left >= cnt_right:
                    answer += 'R'
                    right[0] = location[number][0]
                    right[1] = location[number][1]
                else:
                    answer += 'L'
                    left[0] = location[number][0]
                    left[1] = location[number][1]
    return answer

print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))