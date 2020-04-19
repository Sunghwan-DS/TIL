N, M, D = map(int, input().split())
field_original = []
for _ in range(N):
    field_original.append(list(map(int, input().split())))


result = 0


def defense(field, hunt, index, archer1, archer2, archer3):
    global result
    if index == N:
        if result < hunt:
            result = hunt
        return

    D1 = D+1
    D2 = D+1
    D3 = D+1
    cnt_hunt = 0
    new_field = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            new_field[i][j] = field[i][j]
    for j in range(M):
        for i in range(N):
            if new_field[i][j] == 0:
                continue

            if abs(i-N) + abs(j-archer1) < D1:
                D1 = abs(i-N) + abs(j-archer1)
                target1 = [i, j]

            if abs(i-N) + abs(j-archer2) < D2:
                D2 = abs(i-N) + abs(j-archer2)
                target2 = [i, j]

            if abs(i-N) + abs(j-archer3) < D3:
                D3 = abs(i-N) + abs(j-archer3)
                target3 = [i, j]


    if D1 < D+1:
        new_field[target1[0]][target1[1]] = 0
        cnt_hunt += 1

    if D2 < D+1:
        if new_field[target2[0]][target2[1]] == 1:
            new_field[target2[0]][target2[1]] = 0
            cnt_hunt += 1

    if D3 < D+1:
        if new_field[target3[0]][target3[1]] == 1:
            new_field[target3[0]][target3[1]] = 0
            cnt_hunt += 1

    for i in range(N-2, -1, -1):
        for j in range(M):
            new_field[i+1][j] = new_field[i][j]

    for j in range(M):
        new_field[0][j] = 0

    defense(new_field, hunt+cnt_hunt, index+1, archer1, archer2, archer3)


def archer_position(position, idx):
    if idx == 3:
        defense(field_original, 0, 0, position[0], position[1], position[2])
        return

    if idx == 0:
        for _ in range(M-2):
            position.append(_)
            archer_position(position, idx+1)
            del position[-1]
        return

    for __ in range(M):
        if max(position) >= __:
            continue

        position.append(__)
        archer_position(position, idx+1)
        del position[-1]

archer_position([], 0)
print(result)