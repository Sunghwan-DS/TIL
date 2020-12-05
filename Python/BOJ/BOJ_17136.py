field_original = [list(map(int, input().split())) for _ in range(10)]
result = 26


def pasting(i, j, count, field, use):
    global result
    if i == 9 and j == 9:
        if field[i][j] == 1:
            count += 1
            if use[0] == 5:
                return
        if result > count:
            result = count
        return

    if count == result:
        return

    if field[i][j] == 0:
        if j != 9:
            pasting(i, j + 1, count, field, use)
        elif i != 9:
            pasting(i + 1, 0, count, field, use)

    else:
        TF1 = False
        TF2 = False
        TF3 = False
        TF4 = False

        if max(i, j) <= 8:
            TF1 = True
            for _ in range(1):
                if field[i + _][j + 1] == 0:
                    TF1 = False
                    break
            for _ in range(2):
                if field[i + 1][j + _] == 0:
                    TF1 = False
                    break
        if TF1 and max(i, j) <= 7:
            TF2 = True
            for _ in range(2):
                if field[i + _][j + 2] == 0:
                    TF2 = False
                    break
            for _ in range(3):
                if field[i + 2][j + _] == 0:
                    TF2 = False
                    break
        if TF2 and max(i, j) <= 6:
            TF3 = True
            for _ in range(3):
                if field[i + _][j + 3] == 0:
                    TF3 = False
                    break
            for _ in range(4):
                if field[i + 3][j + _] == 0:
                    TF3 = False
                    break
        if TF3 and max(i, j) <= 5:
            TF4 = True
            for _ in range(4):
                if field[i + _][j + 4] == 0:
                    TF4 = False
                    break
            for _ in range(5):
                if field[i + 4][j + _] == 0:
                    TF4 = False
                    break

        new_use = use[:]
        if TF4 and new_use[4] <= 4:
            new_field = [line[:] for line in field]
            for _ in range(5):
                for __ in range(5):
                    new_field[i + _][j + __] = 0
            new_use[4] += 1
            pasting(i, j + 1, count + 1, new_field, new_use)
            new_use[4] -= 1

        if TF3 and new_use[3] <= 4:
            new_field = [line[:] for line in field]
            for _ in range(4):
                for __ in range(4):
                    new_field[i + _][j + __] = 0
            new_use[3] += 1
            pasting(i, j + 1, count + 1, new_field, new_use)
            new_use[3] -= 1

        if TF2 and new_use[2] <= 4:
            new_field = [line[:] for line in field]
            for _ in range(3):
                for __ in range(3):
                    new_field[i + _][j + __] = 0
            new_use[2] += 1
            pasting(i, j + 1, count + 1, new_field, new_use)
            new_use[2] -= 1

        if TF1 and new_use[1] <= 4:
            new_field = [line[:] for line in field]
            for _ in range(2):
                for __ in range(2):
                    new_field[i + _][j + __] = 0
            new_use[1] += 1
            pasting(i, j + 1, count + 1, new_field, new_use)
            new_use[1] -= 1

        if new_use[0] <= 4:
            new_field = [line[:] for line in field]
            new_field[i][j] = 0
            new_use[0] += 1
            if j != 9:
                pasting(i, j + 1, count + 1, new_field, new_use)
            elif i != 9:
                pasting(i + 1, 0, count + 1, new_field, new_use)
            new_use[0] -= 1


pasting(0, 0, 0, field_original, [0, 0, 0, 0, 0])
if result == 26:
    print("-1")
else:
    print(result)