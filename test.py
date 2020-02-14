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

# N = int(input())
sentence = input()
print(len(sentence) - getpartialmatch(sentence)[-1])
print(list(getpartialmatch(sentence)))