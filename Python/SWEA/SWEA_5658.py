T = int(input())
for case in range(1,T+1):
    N, K = map(int,input().split())
    Alphabet = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    L = N // 4
    data = input()
    nums = []
    for d in data:
        if d in Alphabet:
            nums.append(Alphabet[d])
        else:
            nums.append(int(d))

    ans = set()
    res = 0
    for i in range(0, -L, -1):
        res += nums[i]*16**(-i)
    ans.add(res)

    for i in range(1, N):
        res -= nums[i-L] * 16**(L-1)
        res *= 16
        res += nums[i]
        ans.add(res)

    ans = list(ans)
    ans.sort(reverse=True)

    print("#%d"%(case), ans[K-1])