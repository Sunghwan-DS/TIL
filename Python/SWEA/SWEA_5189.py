from itertools import permutations as permu

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    lst = [i for i in range(1, N)]

    ans = 1000000
    for seq in permu(lst, len(lst)):
        seq = [0] + list(seq) + [0]
        res = 0
        for idx in range(len(seq)-1):
            res += arr[seq[idx]][seq[idx+1]]
        ans = min(ans, res)
    print("#%d"%(tc), ans)