n = int(input())

res = dict()
kind_of_server = []
for _ in range(n):
    date, serverId, charId, point = input().split(', ')
    serverId = serverId[9:]
    charId = int(charId[7:])
    point = int(point[6:])
    if serverId in res:
        if charId in res[serverId]:
            res[serverId][charId] += point
        else:
            res[serverId][charId] = point
    else:
        kind_of_server.append(serverId)
        res[serverId] = dict()
        res[serverId][charId] = point

kind_of_server.sort()
for serverId in kind_of_server:
    print(serverId)
    for_sort = []
    for charId in res[serverId]:
        for_sort.append((res[serverId][charId], charId))

    for_sort.sort(key = lambda x: (-x[0], x[1]))
    last_point = -1
    last_rank = -1
    for idx, tu in enumerate(for_sort):
        point, charId = tu
        if point == last_point:
            print(last_rank + ':' + str(charId) + ':' + str(point))
        else:
            print(str(idx + 1) + ':' + str(charId) + ':' + str(point))
            last_point = point
            last_rank = str(idx + 1)
