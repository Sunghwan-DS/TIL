def BFS(start):
    queue = [start]
    virus = [start]

    while queue:
        i = queue.pop(0)
        for num, j in enumerate(field[i]):
            if j:
                if num not in virus:
                    virus.append(num)
                    queue.append(num)


    return len(virus)


N = int(input())
field = [[0] * (N+1) for _ in range(N+1)]
T = int(input())
for _ in range(T):
    a, b = map(int,input().split())
    field[a][b] = 1
    field[b][a] = 1

print(BFS(1)-1)