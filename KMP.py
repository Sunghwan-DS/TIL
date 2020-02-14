def getpartialmatch(N):
    m = len(N)
    pi = [0] * m
    begin = 1
    matched = 0
    while begin + matched < m:
        if N[begin + matched] == N[matched]:
            matched += 1
            pi[begin + matched - 1] = matched
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched - 1]
                matched = pi[matched - 1]
    return pi


def kmp(p, sen):
    n = len(p)
    m = len(sen)
    pi = getpartialmatch(sen)
    begin = 0
    matched = 0
    ans = 0
    while begin <= n - m:
        if matched < m and p[begin + matched] == sen[matched]:
            matched += 1
            if matched == m:
                ans = 1
                break
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched - 1]
                matched = pi[matched - 1]
    return ans

T = int(input())
for case in range(1, T+1):
    pattern = input()
    sentence = input()
    print("#%d" % (case), kmp(sentence, pattern))