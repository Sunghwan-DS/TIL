def check(group):
    visited = [[False]*5 for _ in range(5)]
    for idx in group:
        visited[idx//5][idx%5] = True

    y, x = group[0]//5, group[0]%5
    s = [(y, x)]
    visited[y][x] = False
    cnt = 0

    while s:
        y, x = s.pop()
        cnt += 1

        for dirc in range(4):
            ny = y + dy[dirc]
            nx = x + dx[dirc]

            if 0 <= ny <= 4 and 0 <= nx <= 4 and visited[ny][nx]:
                visited[ny][nx] = False
                s.append((ny, nx))

    if cnt == 7:
        return True
    else:
        return False


def make_group(group, Y_num):
    global ans
    if Y_num >= 4:
        return

    if len(group) == 7:
        if check(group):
            ans += 1
        return

    if group:
        start = group[-1] + 1
    else:
        start = 0
    end = 19 + len(group)

    for idx in range(start, end):
        group.append(idx)
        if arr[idx//5][idx%5] == 'Y':
            make_group(group, Y_num+1)
        else:
            make_group(group, Y_num)
        group.pop()


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

ans = 0
arr = [list(input()) for _ in range(5)]
make_group([], 0)
print(ans)