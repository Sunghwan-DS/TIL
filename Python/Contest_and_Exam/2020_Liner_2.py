def solution(answer_sheet, sheets):
    answer = 0
    ans_len = len(answer_sheet)
    N = len(sheets)
    for i in range(N-1):
        for j in range(i+1, N):
            res = 0
            max_x = 0
            cnt = 0
            for k in range(ans_len):
                if answer_sheet[k] != sheets[i][k] and sheets[i][k] == sheets[j][k]:
                    res += 1
                    cnt += 1
                else:
                    max_x = max(max_x, cnt)
                    cnt = 0
            max_x = max(max_x, cnt)
            res += max_x ** 2
            answer = max(answer, res)
    return answer

print(solution("24551", ["24553", "24553", "24553", "24553"]))