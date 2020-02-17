for case in range(1, 11):
    data = input()
    stack = []
    sym = {'*' : 2, '+' : 1}
    lst = []
    for l in data:
        if l in sym:
            while stack:


        else:
            lst.append(l)


    print("#%d"%(case), sum(lst))