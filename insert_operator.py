N = int(input())
sequence = list(map(int, input().split()))
operator = list(map(int, input().split()))
max_num = -1000000000
min_num = 1000000000

def go(index, operator, last):
    global max_num, min_num
    if index == N:
        if last > max_num:
            max_num = last
        if last < min_num:
            min_num = last
        return

    if operator[0] != 0:
        last += sequence[index]
        operator[0] -= 1
        go(index+1, operator, last)
        last -= sequence[index]
        operator[0] += 1

    if operator[1] != 0:
        last -= sequence[index]
        operator[1] -= 1
        go(index+1, operator, last)
        last += sequence[index]
        operator[1] += 1

    if operator[2] != 0:
        last *= sequence[index]
        operator[2] -= 1
        go(index+1, operator, last)
        last //= sequence[index]
        operator[2] += 1

    if operator[3] != 0:
        save = last
        last = int(last / sequence[index])
        operator[3] -= 1
        go(index+1, operator, last)
        last = save
        operator[3] += 1

go(1, operator, sequence[0])
print(max_num)
print(min_num)