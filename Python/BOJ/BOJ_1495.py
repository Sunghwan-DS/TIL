N, S, M = map(int, input().split())
V = list(map(int, input().split()))

record = [S]
for v in V:
    next_record = set()
    for num in record:
        if 0 <= num + v <= M:
            next_record.add(num + v)
        if 0 <= num - v <= M:
            next_record.add(num - v)
    if len(next_record) == 0:
        print(-1)
        exit()
    record = next_record

print(max(record))