from collections import deque

def solution(dolls):
    q = deque()
    q.append((0, 0, 0, -1))

    cnt = 0
    for doll in dolls:
        doll_time = doll[0]
        doll_item = doll[1]

        for _ in range(len(q)):
            now = q.popleft()
            print(now, doll_time)
            score, item, item_time, fever = now[0], now[1], now[2], now[3]

            if item_time <= doll_time and item:
                item = 0
                item_time = 0
                fever = item_time + 30
                score += cnt * 10

            if doll_time < fever:
                score += 51
                if doll_item:
                    item = 1
                    item_time = doll_time + 10
                q.append((score, item, item_time, fever))

            elif item and doll_item:
                item = 1
                item_time = doll_time + 10
                fever = doll_time - 0.5 + 30
                score += cnt * 10
                score += 51
                q.append((score, item, item_time, fever))

            else:
                if item:
                    item = 0
                    item_time = 0
                    fever = doll_time - 0.5 + 30
                    score += cnt * 10
                    score += 51
                    q.append((score, item, item_time, fever))

                elif doll_item:
                    score += 1
                    item = 1
                    item_time = doll_time + 10
                    q.append((score, item, item_time, fever))

                else:
                    score += 1
                    q.append((score, item, item_time, fever))

        cnt += 1

    answer = 0
    for data in q:
        answer = max(answer, data[0])
    return answer


print(solution([[5,0],[7,1],[12,0],[16,0],[20,1],[29,1],[35,0],[38,0],[60,0],[72,0]]))
# 510