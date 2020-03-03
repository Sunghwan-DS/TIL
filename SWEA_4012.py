from itertools import combinations

def go(m):
    s = 0
    for i in range(len(m)):
        for j in range(i+1, len(m)):
            s += arr[m[i]][m[j]]
            s += arr[m[j]][m[i]]

    return s

T = int(input())
for case in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    lst = list(combinations([i for i in range(N)], N//2))
    score = []
    ans = 1000000
    for idx in range(len(lst)//2):
        score1 = go(lst[idx])
        score2 = go(lst[len(lst)-1-idx])
        ans = min(ans, abs(score1 - score2))

    print("#%d"%(case), ans)