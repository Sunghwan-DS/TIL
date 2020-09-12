# 15:10 ~ 16:04 + 19:17 ~

def solution(play_time, adv_time, logs):
    from collections import deque
    def cal_time(time):
        h, m, s = time.split(':')
        return 3600 * int(h) + 60 * int(m) + int(s)
    play_time = cal_time(play_time)
    adv_time = cal_time(adv_time)
    new_logs = []
    for log in logs:
        s, e = log.split('-')
        e = cal_time(e)
        s = cal_time(s)
        new_logs.append([e, s])
    new_logs.append([0, 0])
    new_logs.sort()
    for idx, log in enumerate(new_logs):
        log.append(idx)
    answer = ''
    history = deque()
    history.append(new_logs[0])
    max_time = 0
    stop = False
    for log in new_logs:
        end_time, start_time, start_idx = log
        if start_time + adv_time > play_time:
            stop = True
            start_time = play_time - adv_time
        for idx in range(history[-1][2] + 1, len(new_logs)):
            # 새 시작이 지금 끝 보다 작으면 됨
            if new_logs[idx][1] < start_time + adv_time:
                history.append(new_logs[idx])
        time = 0
        while history:
            # 첫 히스토리의 끝나는 시간보다 지금 시작하는 시간이 크면 pop
            if history[0][0] <= start_time:
                history.popleft()
                continue
            else:
                for e, s, idx in history:
                    time += min(e, start_time + adv_time) - max(start_time, s)
                break
        if not history:
            history = deque()
            history.append(new_logs[1])
            continue
        if max_time < time:
            max_time = time
            h = str(start_time // 3600)
            m = str(start_time % 3600 // 60)
            s = str(start_time % 60)
            if len(h) < 2:
                h = '0' + h
            if len(m) < 2:
                m = '0' + m
            if len(s) < 2:
                s = '0' + s
            answer = h + ':' + m + ':' + s
        if stop:
            break
    return answer

ex1 = ("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"])
ex2 = ("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"])
ex3 = ("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"])

print(solution(*ex3))