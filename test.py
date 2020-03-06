for tc in range(1, int(input())+1):
    N = int(input())
    data = list(map(int,input().split()))
    ans = {0}
    for i in data:
        new = set()
        for j in ans:
            new.add(i+j)
        ans = ans | new
    print("#%d"%(tc), len(ans))