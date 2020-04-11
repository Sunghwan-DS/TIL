def check(arr, y, x):
    global ans_TF, N
    # for i in range(N):
    #     print(*arr[i])
    # print()
    row = []
    col = []
    for i in range(N):
        if arr[i][x] > 0:
            if arr[i][x] in col:
                return False
            else:
                col.append(arr[i][x])

    for j in range(N):
        if arr[y][j] > 0:
            if arr[y][j] in row:
                return False
            else:
                row.append(arr[y][j])
    return True


def find_ans(arr, i, j):
    global N, ans, ans_arr, ans_TF
    # for _ in range(N):
    #     print(*arr[_])
    # print(i, j)
    # print()

    if ans_TF:
        return

    if i == N:
        ans = 'POSSIBLE'
        ans_arr = [arr[i][:] for i in range(N)]
        ans_TF = True
        return

    if arr[i][j] == 0:
        for num in range(1, N+1):
            arr[i][j] = num
            if check(arr, i, j):
                if j + 1 == N:
                    find_ans(arr, i+1, 0)
                else:
                    find_ans(arr, i, j+1)
            arr[i][j] = 0
    elif j + 1 == N:
        find_ans(arr, i+1, 0)
    else:
        find_ans(arr, i, j+1)

def make_base(idx, lst):
    global N, K, ans_TF
    if ans_TF:
        return

    if sum(lst) > K:
        return

    if idx == N:
        if sum(lst) == K:
            base = [[0] * N for _ in range(N)]
            for i in range(N):
                base[i][i] = lst[i]
            find_ans(base, 0, 0)
        return

    for num in range(1, N+1):
        lst.append(num)
        make_base(idx+1, lst)
        lst.pop()


for T in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    ans = 'IMPOSSIBLE'
    ans_arr = 0
    ans_TF = False
    make_base(0, [])
    print("Case #%d:"%(T), ans)
    if ans == 'POSSIBLE':
        for i in range(N):
            print(*ans_arr[i])
