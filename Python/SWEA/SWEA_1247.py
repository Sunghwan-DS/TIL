def DFS(idx, client, res):
    global ans
    if idx == len(clients) - 1:
        res += abs(home[0] - clients[client][0]) + abs(home[1] - clients[client][1])
        ans = min(ans, res)
        return

    if res >= ans:
        return

    for next_client in range(len(clients)):
        if not visited[next_client]:
            visited[next_client] = True
            DFS(idx + 1, next_client, res + distances[client][next_client])
            visited[next_client] = False


for tc in range(1, int(input()) + 1):
    N = int(input())
    data = list(map(int, input().split()))
    company = (data[1], data[0])
    home = (data[3], data[2])
    clients = []

    for idx in range(N):
        clients.append((data[idx * 2 + 5], data[idx * 2 + 4]))

    distances = [[0] * len(clients) for _ in range(len(clients))]
    for start in range(len(clients)):
        for end in range(start + 1, len(clients)):
            distance = abs(clients[start][0] - clients[end][0]) + abs(clients[start][1] - clients[end][1])
            distances[start][end] = distance
            distances[end][start] = distance

    ans = 1000000
    visited = [False] * len(clients)
    for idx in range(len(clients)):
        visited[idx] = True
        DFS(0, idx, abs(company[0] - clients[idx][0]) + abs(company[1] - clients[idx][1]))
        visited[idx] = False

    print("#%d"%(tc), ans)