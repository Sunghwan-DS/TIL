def solution(depar, hub, dest, roads):
    can_go = {}
    for road in roads:
        s, e = road
        if s not in can_go:
            can_go[s] = {}
        can_go[s][e] = 1

    def cal_value(start, end):
        res = {}
        s = {}
        s[start] = 1

        while s:
            new_s = {}
            for next in s:
                if next in res:
                    res[next] += s[next]
                else:
                    res[next] = s[next]

                if next in can_go:
                    for nnext in can_go[next]:
                        if nnext in new_s:
                            new_s[nnext] += 1
                        else:
                            new_s[nnext] = 1
            s = new_s
        if end in res:
            return res[end]
        else:
            return 0

    answer = cal_value(depar, hub) * cal_value(hub, dest)
    return answer % 10007

ex1 = 'SEOUL', 'DAEGU', 'YEOSU', [["ULSAN","BUSAN"],["DAEJEON","ULSAN"],["DAEJEON","GWANGJU"],["SEOUL","DAEJEON"],["SEOUL","ULSAN"],["DAEJEON","DAEGU"],["GWANGJU","BUSAN"],["DAEGU","GWANGJU"],["DAEGU","BUSAN"],["ULSAN","DAEGU"],["GWANGJU","YEOSU"],["BUSAN","YEOSU"]]
print(solution(*ex1))