# 18:42 ~ 19:17

def solution(n, s, a, b, fares):
    from collections import deque
    pay = [[0] * (n+1) for _ in range(n+1)]
    for c, d, f in fares:
        pay[c][d] = f
        pay[d][c] = f

    both_visited = [10000000] * (n + 1)
    both_visited[s] = 0

    q = deque()
    q.append((s, 0))

    answer = 10000000
    while q:
        current, tot_money = q.popleft()
        for next, money in enumerate(pay[current]):
            if money > 0:
                new_pay = tot_money + money
                if new_pay < both_visited[next]:
                    both_visited[next] = new_pay
                    q.append((next, tot_money + money))

    for start, both_money in enumerate(both_visited):
        if both_money < answer:
            qa = deque()
            qa.append((start, 0))
            a_visited = [10000000] * (n + 1)
            a_visited[start] = 0
            qb = deque()
            qb.append((start, 0))
            b_visited = [10000000] * (n + 1)
            b_visited[start] = 0

            while qa:
                a_cur, a_tot = qa.popleft()
                for a_next, a_money in enumerate(pay[a_cur]):
                    if a_money > 0:
                        new_pay = a_tot + a_money
                        if new_pay < a_visited[a_next]:
                            a_visited[a_next] = new_pay
                            qa.append((a_next, a_tot + a_money))

            while qb:
                b_cur, b_tot = qb.popleft()
                for b_next, b_money in enumerate(pay[b_cur]):
                    if b_money > 0:
                        new_pay = b_tot + b_money
                        if new_pay < b_visited[b_next]:
                            b_visited[b_next] = new_pay
                            qb.append((b_next, b_tot + b_money))

            answer = min(answer, both_money + a_visited[a] + b_visited[b])

    return answer

ex1 = (6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]) # ans = 82

print(solution(*ex1))