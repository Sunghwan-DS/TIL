T = int(input())
for Count in range(T):
    N, L = map(int, input().split())
    score_list = [0]
    cal_list = [0]
    for _ in range(N):
        score, cal = map(int, input().split())
        F_score_list = score_list[:]
        F_cal_list = cal_list[:]
        if cal > L:
            continue
        for i in range(len(score_list)):
            if cal_list[i] + cal <= L:
                same_case = []
                for ii, val in enumerate(cal_list):
                    if val == cal_list[i]:
                        same_case.append(score_list[ii])
                if same_case:
                    F_score_list[idx] = max(max(same_case), F_score_list[i]) + score

                else:
                    F_score_list.append(score_list[i] + score)
                    F_cal_list.append(cal_list[i] + cal)
        score_list = F_score_list[:]
        cal_list = F_cal_list[:]

    print("#{} {}".format(Count + 1, max(score_list)))