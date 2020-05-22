def find_num(target):
    ans = 0
    check = {}
    check[N] = 1
    record = set()
    record.add(N)
    while True:
        ans += 1
        new_record = set()
        for num in record:
            new = num + 1
            if new <= 1000000 and new not in check:
                check[new] = 1
                if new == target:
                    return ans
                else:
                    new_record.add(new)
            new = num - 1
            if new > 0 and new not in check:
                check[new] = 1
                if new == target:
                    return ans
                else:
                    new_record.add(new)
            new = num * 2
            if new <= 1000000 and new not in check:
                check[new] = 1
                if new == target:
                    return ans
                else:
                    new_record.add(new)
            new = num - 10
            if new > 0 and new not in check:
                check[new] = 1
                if new == target:
                    return ans
                else:
                    new_record.add(new)
            record = new_record

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    print("#%d"%(tc), find_num(M))