def make_pi(N):
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


def kmp(sen, pat):
    n = len(sen)
    m = len(pat)
    pi = make_pi(pat)
    begin = 0
    matched = 0
    ans = 0
    while begin <= n - m:
        if matched < m and sen[begin + matched] == pat[matched]:
            matched += 1
            if matched == m:
                ans += 1
                begin += matched
                matched = 0
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched - 1]
                matched = pi[matched - 1]
    return ans

for tc in range(1, int(input()) + 1):
    A, B = input().split()
    print("#%d %d"%(tc, len(A) - kmp(A, B) * (len(B)-1)))