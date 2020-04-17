# 야근
def solution(n, works):
    works.sort(reverse = True)
    works.append(1)
    idx = 0
    while n > 0:
        if works[idx] < works[idx+1]:
            idx += 1
            if idx == len(works)-1:
                return 0
            works[idx] -= 1
            n -= 1
        else:
            idx = 0
            works[idx] -= 1
            n -= 1
    answer = 0
    for i in works[:-1]:
        answer += i ** 2
    return answer


# 건축사업
def column_check(y, x, arr):
    if y == 0 or arr[y - 1][x] % 2 or arr[y][x - 1] // 2 or arr[y][x] // 2:
        return True
    else:
        return False

def beam_check(y, x, arr):
    if arr[y - 1][x] % 2 or arr[y - 1][x + 1] % 2 or (arr[y][x - 1] // 2 and arr[y][x + 1] // 2):
        return True
    else:
        return False

def solution(n, build_frame):
    arr = [[0] * (n + 1) for _ in range(n + 1)]
    for x, y, a, b in build_frame:
        if b == 1:
            if a == 0:
                if column_check(y, x, arr):
                    arr[y][x] += 1
                else:
                    continue
            else:
                if beam_check(y, x, arr):
                    arr[y][x] += 2
                else:
                    continue
        else:
            if a == 0:
                arr[y][x] -= 1
                if arr[y+1][x]%2:
                    if not column_check(y+1, x, arr):
                        arr[y][x] += 1
                        continue
                if arr[y+1][x-1] // 2:
                    if not beam_check(y+1, x-1, arr):
                        arr[y][x] += 1
                        continue
                if arr[y+1][x] // 2:
                    if not beam_check(y+1, x, arr):
                        arr[y][x] += 1
                        continue
            else:
                arr[y][x] -= 2
                if arr[y][x] % 2:
                    if not column_check(y, x, arr):
                        arr[y][x] += 2
                        continue
                if arr[y][x+1] % 2:
                    if not column_check(y, x+1, arr):
                        arr[y][x] += 2
                        continue
                if arr[y][x-1] // 2:
                    if not beam_check(y, x-1, arr):
                        arr[y][x] += 2
                        continue
                if arr[y][x+1] // 2:
                    if not beam_check(y, x+1, arr):
                        arr[y][x] += 2
                        continue


    answer = []
    for j in range(n+1):
        for i in range(n+1):
            if arr[i][j] % 2:
                answer.append([j, i, 0])
            if arr[i][j] // 2:
                answer.append([j, i, 1])
    return answer