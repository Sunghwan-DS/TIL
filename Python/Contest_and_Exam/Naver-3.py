def solution(n, edges):
    global answer
    def virus(cnt, nodes, no_node):
        global answer
        children = []
        for node in nodes:
            if node != no_node:
                for child in tree[node]:
                    children.append(child)
        now_cnt = cnt + len(nodes) - 1

        if not children:
            answer = min(answer, now_cnt)

        for child in children:
            virus(cnt + len(nodes) - 1, children, child)

    tree = [[] for _ in range(n)]
    for s, e in edges:
        tree[s].append(e)

    answer = 10000000
    virus(1, [0], -1)
    return answer

ex1 = (19, [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [3, 7], [3, 8], [3, 9], [4, 10], [4, 11], [5, 12], [5, 13], [6, 14], [6, 15], [6, 16], [8, 17], [8, 18]])
ex2 = (14, [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [2, 7], [3, 8], [3, 9], [3, 10], [4, 11], [4, 12], [4, 13]])
ex3 = (10, [[0, 1], [0, 2], [1, 3], [2, 4], [2, 5], [2, 6], [3, 7], [3, 8], [3, 9]])
print(solution(*ex2))