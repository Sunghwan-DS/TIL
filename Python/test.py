import math

data = [['9', "102 imp 7", "23 imp 23", "23 click 2","41 imp 23", "50 imp 75", "41 imp 23", "41 click 5", "23 imp 2", "102 click 3"],
        ['8', "102 imp 15", "41 imp 23", "50 imp 75", "23 imp 23", "23 click 2", "41 imp 23", "41 click 5", "23 imp 2"]]

for tc in range(2):
    N = int(data[tc][0])
    machine = {}
    # find_ans = False
    min_s = 1000000
    max_s = -1000000
    tot_V = 0
    cnt_item = 0
    for idx in range(1, N + 1):
        item_id, action, cnt = data[tc][idx].split()

        item_id = int(item_id)
        cnt = int(cnt)

        # if find_ans:
        #     continue

        if item_id not in machine:
            machine[item_id] = [1, 15, 0]
            cnt_item += 1
            new = True
        else:
            new = False
            old_V = machine[item_id][2]

        if action == 'imp':
            machine[item_id][1] += cnt
        elif action == 'click':
            machine[item_id][0] += cnt
            machine[item_id][1] -= cnt

        a, b, v = machine[item_id]
        new_V = a * b / ((a + b + 1) * (a + b) ** 2)
        print(item_id, a, b)

        if new:
            tot_V += new_V
        else:
            tot_V -= old_V
            tot_V += new_V
        print(tot_V, cnt_item)
        machine[item_id][2] = new_V

        Sk = math.log(tot_V / cnt_item)
        min_s = min(min_s, Sk)
        max_s = max(max_s, Sk)
        print(Sk, min_s, max_s)
        # print(Sk - min_s, (max_s - min_s) * 0.05)
        if (Sk - min_s) < (max_s - min_s) * 0.05:
            # find_ans = True
            print('발견', idx)


# 2
# 9
# 102 imp 7
# 23 imp 23
# 23 click 2
# 41 imp 23
# 50 imp 75
# 41 imp 23
# 41 click 5
# 23 imp 2
# 102 click 3
# 8
# 102 imp 15
# 41 imp 23
# 50 imp 75
# 23 imp 23
# 23 click 2
# 41 imp 23
# 41 click 5
# 23 imp 2