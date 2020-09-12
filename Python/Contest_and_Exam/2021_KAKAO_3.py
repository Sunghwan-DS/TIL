#     ~ 15:04 + 17:24 ~ 17:36
# 점수 sorting 한 다음 lower bound

def solution(info, query):
    result = {}
    for data in info:
        lang, fb, js, cp, score = data.split()
        case = lang + fb + js + cp
        if case in result:
            result[case].append(int(score))
        else:
            result[case] = [int(score)]

    for key in result:
        result[key].sort()

    answer = []
    for want in query:
        lang, d1, fb, d2, js, d3, cp, score = want.split()
        if lang == '-':
            langs = ['cpp', 'java', 'python']
        else:
            langs = [lang]
        if fb == '-':
            fbs = ['frontend', 'backend']
        else:
            fbs = [fb]
        if js == '-':
            jss = ['junior', 'senior']
        else:
            jss = [js]
        if cp == '-':
            cps = ['chicken', 'pizza']
        else:
            cps = [cp]

        def lower_bound(lst, target):
            low = 0
            high = len(lst) - 1

            while low < high:
                m = (low + high) // 2
                if lst[m] < target:
                    low = m + 1
                else:
                    high = m
            if lst[high] < target:
                return 'no'
            return high

        def lower_bound(lst, target):
            low = 0
            high = len(lst) - 1

            while low < high:
                m = (low + high) // 2
                if lst[m] < target:
                    low = m + 1
                else:
                    high = m
            if lst[high] < target:
                return len(lst)
            return high

        res = 0
        for lang in langs:
            for fb in fbs:
                for js in jss:
                    for cp in cps:
                        case = lang + fb + js + cp
                        if case in result:
                            res += len(result[case]) - lower_bound(result[case], int(score))

        answer.append(res)
    return answer


ex1 = (["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])
# ans = [1,1,1,1,2,4]

print(solution(*ex1))