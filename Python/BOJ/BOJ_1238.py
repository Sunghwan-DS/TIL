def DFS(current, deep):
    visited[current] = deep
    for next_num in range(1, 101):
        if arr[current][next_num] and deep < visited[next_num]:
            DFS(next_num, deep+1)


for tc in range(1, 11):
    N, start = map(int,input().split())
    data = list(map(int,input().split()))
    arr = [[False] * 101 for _ in range(101)]
    for i in range(0, N, 2):
        arr[data[i]][data[i+1]] = True
    visited = [101] * 101
    DFS(start, 1)
    max_deep = 0
    ans = 0
    for i in range(1, 101):
        if max_deep <= visited[i] < 101:
            max_deep = visited[i]
            ans = i

    print("#%d"%(tc), ans)