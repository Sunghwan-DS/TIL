def make_word(idx, word):
    global b
    if idx == b:
        words.append(word)
        return
    make_word(idx+1, word + '0')
    make_word(idx + 1, word + '1')

t, b = map(int,input())
words = []
make_word(0, '')

for i in words:
    io.PrintOutput(i)
    if io.ReadInput == 'Y':
        exit()