def dt_check(d_num, dt):
    if dt == table_0:
        if d_num == 5:
            return table_5
        elif d_num == 10:
            return table_10
        elif d_num == 15:
            return table_15
        else:
            return dt
    else:
        return dt

def go(d1, d2, d3, d4, idx, score):
    global result, dt1, dt2, dt3, dt4
    if idx == 10:
        if result < score:
            result = score
        return

    n = dice[idx]

    dt1 = dt_check(d1, dt1)
    dt2 = dt_check(d2, dt2)
    dt3 = dt_check(d3, dt3)
    dt4 = dt_check(d4, dt4)


    if dt1[d1+n] == dt2[d2] or dt1[d1+n] == dt3[d3] or dt1[d1+n] == dt4[d4]:
        if dt1[d1+n] == 10 or dt1[d1+n] == 20 or dt1[d1+n] == 30:
            pass
        elif dt1 == dt2 or dt1 == dt3 or dt1 == dt4:
            pass
        else:
            score1 = score + dt1[d1 + n]
            go(d1 + n, d2, d3, d4, idx + 1, score1)
    else:
        score1 = score + dt1[d1 + n]
        go(d1 + n, d2, d3, d4, idx + 1, score1)


    if dt2[d2 + n] == dt1[d1] or dt2[d2 + n] == dt3[d3] or dt2[d2 + n] == dt4[d4]:
        if dt2[d2+n] == 10 or dt2[d2+n] == 20 or dt2[d2+n] == 30:
            pass
        elif dt2 == dt1 or dt2 == dt3 or dt2 == dt4:
            pass
        else:
            score2 = score + dt2[d2 + n]
            go(d1, d2 + n, d3, d4, idx + 1, score2)
    else:
        score2 = score + dt2[d2 + n]
        go(d1, d2 + n, d3, d4, idx + 1, score2)


    if dt3[d3 + n] == dt1[d1] or dt3[d3 + n] == dt2[d2] or dt3[d3 + n] == dt4[d4]:
        if dt3[d3+n] == 10 or dt3[d3+n] == 20 or dt3[d3+n] == 30:
            pass
        elif dt3 == dt1 or dt3 == dt2 or dt3 == dt4:
            pass
        else:
            score3 = score + dt3[d3 + n]
            go(d1, d2, d3 + n, d4, idx + 1, score3)
    else:
        score3 = score + dt3[d3 + n]
        go(d1, d2, d3 + n, d4, idx + 1, score3)


    if dt4[d4 + n] == dt1[d1] or dt4[d4 + n] == dt2[d2] or dt4[d4 + n] == dt3[d3]:
        if dt4[d4 + n] == 10 or dt4[d4 + n] == 20 or dt4[d4 + n] == 30:
            pass
        elif dt4 == dt1 or dt4 == dt2 or dt4 == dt3:
            pass
        else:
            score4 = score + dt4[d4 + n]
            go(d1, d2, d3, d4 + n, idx + 1, score4)
    else:
        score4 = score + dt4[d4 + n]
        go(d1, d2, d3, d4 + n, idx + 1, score4)



dice = list(map(int,input().split()))
table_0 = [2 * i for i in range(21)]
table_5 = [1, 0, 0, 0, 0, 10, 13, 16, 19, 25, 30, 35, 40]
table_10 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 22, 24, 25, 30, 35, 40]
table_15 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30, 28, 27, 26, 25, 30, 35, 40]
table_0[0] = 1

table_0 += [0] * 30
table_5 += [0] * 38
table_10 += [0] * 34
table_15 += [0] * 28

# print(len(table_0), len(table_5), len(table_10), len(table_15))
#
# arr = []
# arr.append(table_0)
# arr.append(table_5)
# arr.append(table_10)
# arr.append(table_15)
#
# for i in range(4):
#     print(arr[i])

dt1 = table_0
dt2 = table_0
dt3 = table_0
dt4 = table_0


# print(len(table_0), len(table_5), len(table_10), len(table_15))


result = 0




go(dice[0], 0, 0, 0, 1, table_0[dice[0]])
print(result)