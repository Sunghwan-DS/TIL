def make_pi(N):
    m = len(N)
    pi = [0] * m        # 어느 지점에서 만들어지는 중복된 최장 문자열
    begin = 1
    matched = 0
    while begin + matched < m:      # begin + match => 검토하고자 하는 현재 위치
        if N[begin + matched] == N[matched]:
            matched += 1
            pi[begin + matched - 1] = matched       # 검토한 자리(begin + match)에 저장하고 싶은데 match가 이미 1 올랐으므로 begin + mathch - 1
        else:
            if matched == 0:        # match 된 적이 없으면 begin만 + 1
                begin += 1
            else:
                begin += matched - pi[matched - 1]      # 검토할 자리를 얼마나 이동할 것인가? => 현재 매칭값 - 이전의 최장 길이
                matched = pi[matched - 1]       # 현재 매칭값은 이전의 최장 중복 문자열로 이동
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