def solution(n, path, order):
    visited = {}
    cant = {}
    connection = [[[], -1, -1] for _ in range(n)] # 연결된 곳, 필요한 곳, 필요로 하는 곳
    for s, e in path:
        connection[s][0].append(e)
        connection[e][0].append(s)

    for s, e in order:
        connection[e][1] = s
        connection[s][2] = e

    if connection[0][1] != -1:
        return False

    stack = [0]
    visited[0] = 1
    while stack:
        now = stack.pop()
        for child in connection[now][0]:
            if child in visited:
                pass

            elif connection[child][1] == -1 or connection[child][1] in visited:
                visited[child] = 1
                stack.append(child)
                need = connection[child][2]
                if need != -1 and need in cant:
                    visited[need] = 1
                    stack.append(need)
                    del cant[need]

            else:
                cant[child] = 1

    if len(visited) != n:
        return False
    else:
        return True