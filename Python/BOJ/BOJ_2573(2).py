class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_List:
    def __init__(self):
        dummy = Node("dummy")
        self.head = dummy
        self.tail = dummy
        self.current = None
        self.before = None
        self.num_of_data = 0

    def append(self, data):
        new = Node(data)
        self.tail.next = new
        self.tail = new
        self.num_of_data += 1

    def front(self):
        self.current = self.head
        self.before = None

    def next(self):
        self.before = self.current
        self.current = self.current.next

    def pop(self):
        self.before.next = self.current.next
        self.current = self.before
        self.num_of_data -= 1


def check(y, x):
    global N, M
    cnt = 1
    visited = [[False] * M for _ in range(N)]
    visited[y][x] = True

    s = [(y, x)]

    while s:
        y, x = s[-1]

        for dir in range(4):
            ny = y + dy[dir]
            nx = x + dx[dir]

            if not visited[ny][nx] and arr[ny][nx] != 0:
                s.append((ny,nx))
                visited[ny][nx] = True
                cnt += 1
                break

        else:
            s.pop()
    return cnt


N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
melt = [[0] * M for _ in range(N)]
dy = [-1, 0 , 1, 0]
dx = [0, 1, 0, -1]

ice = Linked_List()
for i in range(N):
    for j in range(M):
        if arr[i][j] != 0:
            ice.append((i, j))

ans = 0
cnt = 0
while ice.num_of_data:
    y, x = ice.head.next.data
    if ice.num_of_data != check(y, x):
        ans = cnt
        break
    cnt += 1

    ice.front()
    for i in range(ice.num_of_data):
        ice.next()
        y, x = ice.current.data
        m = 0

        for dir in range(4):
            ny = y + dy[dir]
            nx = x + dx[dir]

            if arr[ny][nx] == 0:
                melt[y][x] += 1

    ice.front()
    for i in range(ice.num_of_data):
        ice.next()
        y, x = ice.current.data
        if arr[y][x] - melt[y][x] <= 0:
            arr[y][x] = 0
            ice.pop()
        else:
            arr[y][x] -= melt[y][x]

        melt[y][x] = 0

print(ans)