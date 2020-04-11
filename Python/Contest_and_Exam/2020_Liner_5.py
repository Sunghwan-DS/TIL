def solution(dataSource, tags):
    answer = []
    arr = [[] for _ in range(len(tags) + 1)]

    for data in dataSource:
        cnt = 0
        name = data[0]
        for i in range(1, len(data)):
            if data[i] in tags:
                cnt += 1
        arr[cnt].append(name)

    for i in range(len(tags), 0, -1):
        arr[i].sort()
        answer.extend(arr[i])
        if len(answer) >= 10:
            break

    return answer[:10]

print(solution([
    ["doc1", "t1", "t2", "t3"],
    ["doc2", "t0", "t2", "t3"],
    ["doc3", "t1", "t6", "t7"],
    ["doc4", "t1", "t2", "t4"],
    ["doc5", "t6", "t100", "t8"]
], ["t1", "t2", "t3"]))