from collections import deque

def solution(land, height):
    def choose(idx, lst):
        global answer
        if len(lst) == num - 2:
            answer = min(answer, check(lst))
            return
        if idx == len(roads):
            return

        lst.append(roads[idx])
        choose(idx + 1, lst)
        lst.pop()
        choose(idx + 1, lst)

    def labeling(y, x):
        label[y][x] = num

        q = deque()
        q.append((y, x))

        dy = (-1, 0, 1, 0)
        dx = (0, 1, 0, -1)

        while q:
            y, x = q.popleft()
            for dirc in range(4):
                ny = y + dy[dirc]
                nx = x + dx[dirc]
                if 0 <= ny <= N-1 and 0 <= nx <= N-1:
                    if abs(land[y][x] - land[ny][nx]) <= height and not label[ny][nx]:
                        label[ny][nx] = num
                        q.append((ny, nx))


    N = len(land)
    label = [[0] * N for _ in range(N)]

    num = 1
    for i in range(N):
        for j in range(N):
            if not label[i][j]:
                labeling(i, j)
                num += 1

    connection = [[0] * num for _ in range(num)]
    for y in range(N):
        for x in range(N):
            for dy, dx in ((0, 1), (1, 0)):
                ny = y + dy
                nx = x + dx

                if 0 <= ny <= N-1 and 0 <= nx <= N-1:
                    l1 = label[y][x]
                    l2 = label[ny][nx]
                    if l1 != l2:
                        price = abs(land[y][x] - land[ny][nx])
                        if not connection[l1][l2]:
                            connection[l1][l2] = price
                        else:
                            connection[l1][l2] = min(connection[l1][l2], price)

                        if not connection[l2][l1]:
                            connection[l2][l1] = price
                        else:
                            connection[l2][l1] = min(connection[l2][l1], price)

    for i in range(num):
        print(connection[i])
    print()

    answer = 0
    roads = []
    for i in range(1, num):
        for j in range(i + 1, num):
            if connection[i][j]:
                roads.append((i, j))
    choose(0, [])

    return answer





# print(solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]], 3))
print(solution([[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]], 1))