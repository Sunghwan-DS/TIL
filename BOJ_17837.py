def move():
    for idx, u in enumerate(units):
        y = u[0]
        x = u[1]
        dir = u[2]

        ny = y + dy[dir]
        nx = x + dx[dir]

        if 0 <= ny <= N-1 and 0 <= nx <= N-1:
            if arr[ny][nx] == 0:
                a = 999999
                lst = []
                while a != idx:
                    a = arr[y][x].pop()
                    lst.insert(0, a)

                for num in lst:
                    units[num-1][0] = ny
                    units[num-1][1] = nx
                arr[ny][nx].extend(lst)

            elif arr[ny][nx] == 1:
                a = 999999
                lst = []
                while a != idx:
                    a = arr[y][x].pop()
                    lst.append(a)
                for num in lst:
                    units[num-1][0] = ny
                    units[num-1][1] = nx
                arr[ny][nx].extend(lst)

            elif arr[ny][nx] == 2:
                if arr[y-dy[dir]][x-dx[dir]] ==



def minus1(num):
    return num-1


N, K = map(int,input().split())
color = [list(map(int,input().split())) for _ in range(N)]
arr = [[[] for __ in range(N)] for _ in range(N)]
# for _ in range(N):
#     print(arr[_])
# print()
units = [list(map(minus1,map(int,input().split()))) for _ in range(K)]

print(units)
for idx, i in enumerate(units):
    arr[i[0]][i[1]].append(idx)

for _ in range(N):
    print(arr[_])
print()


dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

