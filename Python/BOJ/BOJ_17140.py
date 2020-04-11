def counting(lst):
    table = [0] * 101
    for i in lst:
        table[i] += 1
    table[0] = 0
    table2 = table[:]
    table2.sort()
    result = []
    for i in table2:
        if i == 0:
            pass
        else:
            result.append((table.index(i), i))
            table[table.index(i)] = 0
    return result


def go():
    global max_col
    for rows in arr:
        next_row = []
        count_table = counting(rows)
        for num, cnt in count_table:
            if num == 0:
                continue
            next_row.append(num)
            next_row.append(cnt)
        max_col = max(max_col, len(next_row))
        next_arr.append(next_row)

    for rows in next_arr:
        if len(rows) < max_col:
            for _ in range(max_col - len(rows)):
                rows.append(0)

r, c, k = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(3)]
time = 0

while time <= 100:
    if r <= len(arr) and c <= len(arr[0]) and arr[r-1][c-1] == k:
        print(time)
        break

    time += 1
    max_col = 0
    next_arr = []

    if len(arr) >= len(arr[0]):
        go()
        arr = next_arr

    elif len(arr) < len(arr[0]):
        arr = list(map(list, zip(*arr)))
        go()
        arr = next_arr
        arr = list(map(list, zip(*arr)))

if time == 101:
    print(-1)