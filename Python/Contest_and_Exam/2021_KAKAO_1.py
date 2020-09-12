# 14:00 ~ 14:17

def solution(new_id):
    filter = {'a':1, 'b':1, 'c':1, 'd':1, 'e':1, 'f':1, 'g':1, 'h':1, 'i':1, 'j':1, 'k':1, 'l':1, 'm':1, 'n':1, 'o':1,
              'p':1, 'q':1, 'r':1, 's':1, 't':1, 'u':1, 'v':1, 'w':1, 'x':1, 'y':1, 'z':1, '1':1, '2':1, '3':1, '4':1,
              '5':1, '6':1, '7':1, '8':1, '9':1, '0':1, '-':1, '_':1, '.':1}

    new_id = new_id.lower()
    new_id = list(new_id)
    for idx in range(len(new_id)-1, -1, -1):
        if new_id[idx] not in filter:
            new_id.pop(idx)
    check = 0
    for idx in range(len(new_id)-1, -1, -1):
        if new_id[idx] == '.':
            if check:
                new_id.pop(idx)
            else:
                check = 1
        else:
            check = 0

    if new_id and new_id[0] == '.':
        new_id.pop(0)
    if new_id and new_id[-1] == '.':
        new_id.pop(-1)

    if not new_id:
        new_id = ['a']

    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id.pop(-1)

    save = new_id[-1]
    while len(new_id) <= 2:
        new_id += save

    answer = ''.join(new_id)

    return answer

ex1 = "...!@BaT#*..y.abcdefghijklm"
ex2 = "z-+.^."

print(solution(ex1))