import math

for tc in range(int(input())):
    N = int(input())
    machine = {}
    find_ans = False
    min_s = 1000000
    max_s = -1000000
    tot_V = 0
    cnt_item = 0
    for idx in range(1, N + 1):
        item_id, action, cnt = data[tc][idx].split()
        if find_ans:
            continue

        item_id = int(item_id)
        cnt = int(cnt)


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

        if new:
            tot_V += new_V
        else:
            tot_V -= old_V
            tot_V += new_V

        machine[item_id][2] = new_V

        Sk = math.log(tot_V / cnt_item)
        min_s = min(min_s, Sk)
        max_s = max(max_s, Sk)

        # print(Sk - min_s, (max_s - min_s) * 0.05)
        if (Sk - min_s) < (max_s - min_s) * 0.05:
            find_ans = True
            print(idx)