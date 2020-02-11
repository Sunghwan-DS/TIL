N, K = map(int,input().split())
color = [list(map(int,input().split())) for _ in range(N)]
arr = [[[] for __ in range(N)] for _ in range(N)]
# for _ in range(N):
#     print(arr[_])
# print()
unit = [list(map(int,input().split())) for _ in range(K)]

for idx, i in enumerate(unit):
    arr[i[0]-1][i[1]-1].append(idx)

for _ in range(N):
    print(arr[_])
print()


dy = [0, 0, 0, -1, 1]
dx = [0, 1, -1, 0, 0]

