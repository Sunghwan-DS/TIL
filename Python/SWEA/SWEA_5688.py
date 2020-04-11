prime_nums = [2]
for i in range(3, 1000000):
    for p in prime_nums:
        if i < p**2:
            prime_nums.append(i)
            break
        if i % p == 0:
            break
    else:
        prime_nums.append(i)

for tc in range(1, int(input()) + 1):
    N = int(input())
    result = []
    ans = -1
    TF = True
    for p in prime_nums:
        if N == 1:
            break

        if N < p ** 3:
            TF = False
            break

        if N % p == 0:
            cnt = 1
            N //= p

            while N % p == 0:
                N //= p
                cnt += 1

            if cnt % 3 != 0:
                TF = False
                break
            else:
                result.append((p, cnt // 3))

    if TF:
        ans = 1
        for p, cnt in result:
            ans = ans * p ** cnt

    print("#%d"%(tc), ans)