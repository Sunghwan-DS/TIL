def cal_key(word):
    global dic
    key = 0
    for i, c in enumerate(word):
        mul = 1
        for _ in range(i):
            mul = mul * 62 % 200009
        key += (mul * dic[c]) % 200009
    key %= 200009
    return key


def solution(snapshots, transactions):
    global dic
    ID = [False] * 100000
    hash_table = [[] for _ in range(200009)]
    dic = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'a': 10, 'b': 11, 'c': 12,
           'd': 13, 'e': 14, 'f': 15, 'g': 16, 'h': 17, 'i': 18, 'j': 19, 'k': 20, 'l': 21, 'm': 22, 'n': 23, 'o': 24,
           'p': 25, 'q': 26, 'r': 27, 's': 28, 't': 29, 'u': 30, 'v': 31, 'w': 32, 'x': 33, 'y': 34, 'z': 35, 'A': 36,
           'B': 37, 'C': 38, 'D': 39, 'E': 40, 'F': 41, 'G': 42, 'H': 43, 'I': 44, 'J': 45, 'K': 46, 'L': 47, 'M': 48,
           'N': 49, 'O': 50, 'P': 51, 'Q': 52, 'R': 53, 'S': 54, 'T': 55, 'U': 56, 'V': 57, 'W': 58, 'X': 59, 'Y': 60,
           'Z': 61}

    for idx, lst in enumerate(snapshots):
        lst[1] = int(lst[1])
        hash_table[cal_key(lst[0])].append((lst[0], idx))

    for Id, act, name, cash in transactions:
        if ID[int(Id)]:
            continue
        else:
            ID[int(Id)] = True
            key = cal_key(name)
            for n, i in hash_table[key]:
                if n == name:
                    idx = i
                    break
            else:
                idx = len(snapshots)
                hash_table[key].append((name, idx))
                snapshots.append([name, 0])
            if act == 'SAVE':
                snapshots[idx][1] += int(cash)
            else:
                snapshots[idx][1] -= int(cash)

    for lst in snapshots:
        lst[1] = str(lst[1])

    snapshots.sort()
    return snapshots

print(solution([
  ["ACCOUNT1", "100"],
  ["ACCOUNT2", "150"]
], [
  ["1", "SAVE", "ACCOUNT2", "100"],
  ["2", "WITHDRAW", "ACCOUNT1", "50"],
  ["1", "SAVE", "ACCOUNT2", "100"],
  ["4", "SAVE", "ACCOUNT3", "500"],
  ["3", "WITHDRAW", "ACCOUNT2", "30"]
]))