def check(lst):
    cnt = 0
    for idx in range(10):
        if lst[idx]:
            cnt += 1
            if cnt == 3:
                return True
            if lst[idx] == 3:
                return True
        else:
            cnt = 0
    return False


def game():
    for idx, data in enumerate(datas):
        if idx%2 == 0:
            A[data] += 1
            if check(A):
                return 1
        else:
            B[data] += 1
            if check(B):
                return 2
    return 0


for tc in range(1, int(input()) + 1):
    datas = list(map(int,input().split()))
    A = [0] * 10
    B = [0] * 10
    print("#%d"%(tc), game())