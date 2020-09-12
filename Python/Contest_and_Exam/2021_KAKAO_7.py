# 17:44 ~

def solution(sales, links):
    N = len(sales) + 1
    tree = [[] for _ in range(N)]
    sales.insert(0, 0)
    for a, b in links:
        tree[a].append(b)
    def DFS(current):
        visited[current] = True
        s = [current]
        DP[current][0] = sales[current]
        while s:
            current = s[-1]
            for next in tree[current]:
                if not visited[next]:
                    s.append(next)
                    visited[next] = True
                    break

            else:
                DP[current][0] = sales[current]
                min_val = 1000000
                for child in tree[s[-1]]:
                    DP[s[-1]][0] += DP[child][1]
                    DP[s[-1]][1] += DP[child][1]
                    min_val = min(DP[child][0] - DP[child][1], min_val)
                    if min_val < 0:
                        DP[s[-1]][0] += min_val
                if min_val != 1000000:
                    DP[s[-1]][1] += min_val
                s.pop()

    DP = [[0, 0] for _ in range(N)]
    visited = [False] * N
    DFS(1)
    answer = min(DP[1][0], DP[1][1])
    print(DP)
    print(visited)
    return answer

ex1 = ([14, 17, 15, 18, 19, 14, 13, 16, 28, 17], [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]) # ans = 44
ex4 = ([10, 10, 1, 1], [[3,2], [4,3], [1,4]]) # ans = 2

ex2 = ([20000], [])

print(solution(*ex1))