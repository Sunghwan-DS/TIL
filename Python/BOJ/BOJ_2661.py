def make_sequence(word):
    global ans, find_ans, N
    if find_ans:
        return

    for length in range(2, len(word)//2+1):
        if word[-length*2:-length] == word[-length:]:
            return

    if len(word) == N:
        ans = word
        find_ans = True
        return

    for i in range(1, 4):
        if word[-1] != str(i):
            make_sequence(word + str(i))


N = int(input())
find_ans = False
ans = -1
make_sequence('1')
print(ans)