for tc in range(1, int(input()) + 1):
    word = input()
    res = [0] * (len(word) + 1)
    input()
    H_lst = list(map(int,input().split()))
    for i in H_lst:
        res[i] += 1

    ans = ''
    for i in range(len(word)):
        ans = ans + '-' * res[i] + word[i]

    if res[len(word)]:
        ans += '-' * res[len(word)]

    print("#%d"%(tc), ans)