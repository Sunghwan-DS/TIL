# 2020.03.07
# 20:43 ~ 21:21
# 시뮬레이션 구현
# 시간:60ms, 코드 길이:847B

magnets = [[]]
for i in range(4):
    magnets.append(list(input()))
K = int(input())

for _ in range(K):
    rotation = [False] * 5
    idx, dir = map(int,input().split())
    rotation[idx] = True
    for i in range(idx, 1, -1):
        if magnets[i][-2] != magnets[i-1][2]:
            rotation[i-1] = True
        else:
            break

    for i in range(idx, 4):
        if magnets[i][2] != magnets[i+1][-2]:
            rotation[i+1] = True
        else:
            break

    for i in range(1, 5):
        if rotation[i]:
            if (-1) ** (abs(i-idx)) * dir == 1:
                a = magnets[i].pop()
                magnets[i].insert(0, a)
            else:
                a = magnets[i].pop(0)
                magnets[i].append(a)

ans = 0
for i in range(1, 5):
    if magnets[i][0] == '1':
        ans += 2 ** (i - 1)
print(ans)