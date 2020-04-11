# 2020.04.03
# 14:54 ~ 15:21
# 시뮬레이션 구현
# 시간:4264ms, 코드 길이:1752B

def go(c):
    global pointer, sm, data_idx, si, code_idx, sc, max_code_idx
    if c == '-':
        arr[pointer] -= 1
        if arr[pointer] == -1:
            arr[pointer] = 255
    elif c == '+':
        arr[pointer] += 1
        if arr[pointer] == 256:
            arr[pointer] = 0
    elif c == '<':
        pointer -= 1
        if pointer == -1:
            pointer = sm-1
    elif c == '>':
        pointer += 1
        if pointer == sm:
            pointer = 0
    elif c == '[':
        if arr[pointer] == 0:
            code_idx = teleport[code_idx]
    elif c == ']':
        if arr[pointer] != 0:
            code_idx = teleport[code_idx]
    elif c == '.':
        pass
    elif c == ',':
        if data_idx < si:
            arr[pointer] = ord(data[data_idx])
            data_idx += 1
        else:
            arr[pointer] = 255
    code_idx += 1
    max_code_idx = max(max_code_idx, code_idx)


def Loops_check():
    global code_idx, sc, max_code_idx
    cnt = 0
    while code_idx <= sc-1:
        cnt += 1
        go(code[code_idx])
        if cnt >= 50000000:
            print("Loops", teleport[max_code_idx], max_code_idx)
            return
    print("Terminates")
    return

cnt = 0
for tc in range(1, int(input()) + 1):
    sm, sc, si = map(int,input().split())
    arr = [0] * sm
    pointer = 0
    code = input()
    code_idx = 0
    data = input()
    data_idx = 0

    teleport = [0] * sc
    save = [-1] * (sc//2)

    cnt = 0
    for idx, c in enumerate(code):
        if c == '[':
            save[cnt] = idx
            cnt += 1
        elif c == ']':
            cnt -= 1
            teleport[save[cnt]] = idx
            teleport[idx] = save[cnt]
            save[cnt] = -1
    max_code_idx = 0
    Loops_check()