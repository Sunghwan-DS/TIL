def hanoi(index, start, middle, end):
    if index == 1:
        print("%d %d"%(start, end))
        return

    else:
        hanoi(index-1, start, end, middle)
        print("%d %d"%(start, end))
        hanoi(index-1, middle, start, end)

hanoi(5, 1, 2, 3)