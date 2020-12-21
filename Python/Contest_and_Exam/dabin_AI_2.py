# 1 <= N, M <= 10000000

from itertools import permutations as pm
n, m = input().split()
s, e = len(n), len(m)
n, m = int(n), int(m)

ans = 0

need = [(1, 9), (2, 8), (3, 7), (4, 6)]
for idx in range(s, e+1):
    for num_of_set in range(idx//2 + 1):
        zf = idx - 2 * num_of_set
        def make_sequence(lst, remain, idx):
            def add_remain(lst, zf):
                global ans
                my_lst = []
                for idx, val in enumerate(lst):
                    for _ in range(val):
                        for num in need[idx]:
                            my_lst.append(num)

                for num in range(0, zf + 1):
                    cal_set = set()
                    for _ in range(num):
                        my_lst.append(0)
                    for _ in range(zf - num):
                        my_lst.append(5)
                    # print(my_lst)
                    for my_set in pm(my_lst):
                        my_str = ''
                        for num in my_set:
                            my_str = my_str + str(num)
                        if my_str[0] == '0':
                            continue
                        else:
                            my_num = int(my_str)
                            cal_set.add(my_num)

                    for cal in cal_set:
                        if n <= cal <= m:
                            ans += 1

                    for _ in range(zf):
                        my_lst.pop()


            if idx == 3:
                lst[3] += remain
                add_remain(lst, zf)
                lst[3] -= remain
                return

            for num in range(0, remain+1):
                lst[idx] += num
                make_sequence(lst, remain-num, idx+1)
                lst[idx] -= num

        make_sequence([0, 0, 0, 0], num_of_set, 0)

print(ans)



