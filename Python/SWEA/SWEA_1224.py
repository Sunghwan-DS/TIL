for tc in range(1, int(input()) + 1):
    num, k = map(int, input().split())
    ans = 0
    lst = [num]
    cnt = 0
    while True:
        cnt += 1
        new_set = set()
        for num in lst:
            num = list(str(num))
            for front in range(len(num)):
                for back in range(front + 1, len(num)):
                    new = num[:]
                    new[front], new[back] = new[back], new[front]

                    new_set.add(int(''.join(new)))

        if cnt != k:
            lst = list(new_set)
        else:
            break

    ans = max(new_set)
    print("#%d"%(tc), ans)