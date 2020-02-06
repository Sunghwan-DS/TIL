def rotation(x, d, k):
    global N, M
    for i in range(N):
        if (i+1) % x == 0:
            if d == 0:
                for _ in range(k):
                    a = arr[i].pop(-1)
                    arr[i].insert(0, a)

            elif d == 1:
                for _ in range(k):
                    a = arr[i].pop(0)
                    arr[i].append(a)
    lst = []
    for j in range(M):
        if arr[x][j] != 0:
            if x-1 >= 0:
                if arr[x-1][j] == arr[x][j]:
                    arr[x-1][j] = 0
                    lst.append([x,j])

            if x+1 <=N-1:
                if arr[x][j] == arr[x+1][j]:
                    arr[x+1][j] = 0
                    lst.append([x, j])

    if len(lst) == 0:
        for i in range(N):
            for j in range(M):
                if arr[i][j] != 0:
                    arr[i][j] += 1
    else:
        for co in lst:
            arr[co[0]][co[1]] = 0



N, M, T =map(int,input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int,input().split())))



# x, d, k = map(int,input().split())
# for i in range(N):
#     if (i + 1) % x == 0:
#         if d == 0:
#             for _ in range(k):
#                 a = arr[i].pop(-1)
#                 arr[i].insert(0, a)
#
#         elif d == 1:
#             for _ in range(k):
#                 a = arr[i].pop(0)
#                 arr[i].append(a)
# lst = []
# for j in range(M):
#     if arr[x][j] != 0:
#         if x - 1 >= 0:
#             if arr[x - 1][j] == arr[x][j]:
#                 arr[x - 1][j] = 0
#                 lst.append([x, j])
#
#         if x + 1 <= N - 1:
#             if arr[x][j] == arr[x + 1][j]:
#                 arr[x + 1][j] = 0
#                 lst.append([x, j])
#
# if len(lst) == 0:
#     for i in range(N):
#         for j in range(M):
#             if arr[i][j] != 0:
#                 arr[i][j] += 1
# else:
#     for co in lst:
#         arr[co[0]][co[1]] = 0




for _ in range(T-1):
    x, d, k = map(int,input().split())
    rotation(x, d, k)

result = 0
for i in range(N):
    result += sum(arr[i])

print(result)