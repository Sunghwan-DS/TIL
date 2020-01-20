field = [list(map(int, input().split())) for _ in range(9)]
check = [False] * 27    # 가로줄 9개, 세로줄 9게, 사각형 9개에 대한 체크리스트 27개
line_check = [False] * 10    # 0자리도 포함하여 1부터 9까지 이미 사용한 숫자를 체크하기 위한 리스트

while False in check:
    for i, horizontal_TF in enumerate(check[0:9]):    # horizontal_TF 는 n번 째 가로줄이 완성되있는가를 True, False로 표기
        if horizontal_TF:
            continue

        if field[i].count(0) == 0:
            check[i] = True
            continue

        if field[i].count(0) == 1:
            for _ in range(9):
                line_check[field[i][_]] = True

            field[i][field[i].index(0)] = line_check.index(False)
            check[i] = True
            line_check = [False] * 10
        else:
            pass

    for i, verticle_TF in enumerate(check[9:18]):   # verticle_TF 는 n번 째 세로줄이 완성되있는가를 True, False로 표기
        if verticle_TF:
            continue
        count_zero = 0
        for _ in range(9):
            if field[_][i] == 0:
                count_zero += 1

        if count_zero == 0:
            check[i + 9] = True
            continue

        if count_zero == 1:
            t = 0
            for _ in range(9):
                line_check[field[_][i]] = True
                if field[_][i] != 0:
                    t += 1
                else:
                    tt = t
            field[tt][i] = line_check.index(False)
            check[i+9] = True
            line_check = [False] * 10
        else:
            pass

    for i, square_TF in enumerate(check[18:]):    # square_TF 는 n번 째 3*3이 완성되있는가를 True, False로 표기
        if square_TF:
            continue


        count_zero = 0
        for y in range(i // 3 * 3, i // 3 * 3 + 3):
            for x in range(i % 3 * 3, i % 3 * 3 + 3):
                if field[y][x] == 0:
                    count_zero += 1

        if count_zero == 0:
            check[i + 18] = True
            continue

        if count_zero == 1:
            t = 0
            for y in range(i // 3 * 3, i // 3 * 3 + 3):
                for x in range(i % 3 * 3, i % 3 * 3 + 3):
                    line_check[field[y][x]] = True
                    if field[y][x] != 0:
                        t += 1
                    else:
                        tt = t
            field[i // 3 * 3 + tt // 3][i % 3 * 3 + tt % 3] = line_check.index(False)
            check[i + 18] = True
            line_check = [False] * 10

        else:
            pass

for _ in range(9):
    print(" ".join([str(i) for i in field[_]]))