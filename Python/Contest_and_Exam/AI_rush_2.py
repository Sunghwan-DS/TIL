def solution(n, cars, links):
    tree = [[] for _ in range(n+1)]
    for link in links:
        a, b = link[0], link[1]
        tree[a].append(b)
        tree[b].append(a)

    answer = 10000000
    tot = sum(cars)

    for target in links:
        visited =[False] * (n + 1)
        res1 = 0

        stack = [1]
        visited[1] = True
        while stack:
            cur = stack.pop()
            res1 += cars[cur - 1]

            for child in tree[cur]:
                if cur in target and child in target:
                    continue
                if not visited[child]:
                    visited[child] = True
                    stack.append(child)

        result = abs(tot - res1 * 2)
        answer = min(answer, result)

    return answer

print(solution(13, [22, 9, 1, 15, 8, 6, 20, 7, 11, 5, 10, 4, 1], [[4, 7], [13, 10], [6, 3], [7, 1], [6, 12], [5, 11], [5, 6], [5, 10], [9, 8], [8, 11], [8, 2], [7, 8]]))
