# 12:06 ~ 12:45

def solution(companies, applicants):
    import heapq

    temporary = {}
    c_temporary = {}
    fail = {}

    c_w = {}
    c_n = {}
    a_w = {}
    a_names = []
    c_names = []

    for data in companies:
        name, want, need = data.split()
        c_names.append(name)
        c_w[name] = {}
        c_temporary[name] = {}
        for idx, c in enumerate(want):
            c_w[name][c] = -idx
        c_n[name] = int(need)

    for data in applicants:
        name, want, need = data.split()
        a_names.append(name)
        fail[name] = {}
        need = int(need)
        a_w[name] = []
        for c in want:
            a_w[name].append(c)
            if len(a_w[name]) == need:
                break

    again = True
    while again:
        again = False
        for a_name in a_names:
            if a_name not in temporary:
                for c_name in a_w[a_name]:
                    if c_name not in fail[a_name]:
                        again = True
                        temporary[a_name] = 1
                        c_temporary[c_name][a_name] = 1
                        break

        for c_name in c_names:
            select = []
            cnt = 0
            need = c_n[c_name]

            save = []
            for key in c_temporary[c_name]:
                save.append(key)

            for a_name in save:
                if cnt < need:
                    heapq.heappush(select, (c_w[c_name][a_name], a_name))
                    cnt += 1
                else:
                    heapq.heappush(select, (c_w[c_name][a_name], a_name))
                    val, fail_name = heapq.heappop(select)
                    fail[fail_name][c_name] = 1
                    del temporary[fail_name]
                    del c_temporary[c_name][fail_name]

    answer = []
    for c_name in c_temporary:
        res = c_name + '_'
        lst = []
        for a_name in c_temporary[c_name]:
            lst.append(a_name)
        lst.sort()
        res += ''.join(lst)
        answer.append(res)

    answer.sort()
    return answer


ex1 = (["A fabdec 2", "B cebdfa 2", "C ecfadb 2"], ["a BAC 1", "b BAC 3", "c BCA 2", "d ABC 3", "e BCA 3", "f ABC 2"])
# ans = ["A_bf", "B_ce", "C_d"]
ex2 = (["A abc 2", "B abc 1"], ["a AB 1", "b AB 1", "c AB 1"])
# ans = ["A_ab", "B_"]

print(solution(*ex1))