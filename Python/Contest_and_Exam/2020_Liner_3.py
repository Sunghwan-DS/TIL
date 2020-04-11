def solution(road, n):
    data = []
    cnt = 0
    for c in road:
        if c == '1':
            cnt += 1
        else:
            data.append(cnt)
            cnt = 0
    if len(data) <= n + 1:
        return sum(data) + len(data)
    else:
        res = sum(data[0:n + 1])
        ans = res
        for i in range(n + 1, len(data)):
            res += data[i]
            res -= data[i - (n + 1)]
            ans = max(ans, res)
        return ans + n

print(solution("00110101100111100", 100))