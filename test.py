def make(idx, lst):     # n C r
    if len(lst) == 3:     # r
        print(lst)
        return

    if idx == 5:
        return

    lst.append(seq[idx])
    make(idx+1, lst)
    lst.pop()
    make(idx+1, lst)



seq = [i for i in range(1, 6)]  # [1, 2, 3, 4 ,5]   =>  n


make(0, [])