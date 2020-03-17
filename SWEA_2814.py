for tc in range(1, int(input()) + 1):
    N, M = map(int,input().split())
    arr = [[False] * (N+1) for _ in range(N+1)]
    for i in range(M):
        s, e = map(int,input().split())
        arr[s][e] = True
        arr[e][s] = True

    ans = 0
    for i in range(1, N+1):
        now_visited = [False] * (N+1)
        now_visited[i] = True
        val_lst = [1] * (N + 1)

        s = [i]
        cnt = 0
        while s:
            now = s[-1]
            cnt += 1
            print(now, cnt)
            for j in range(1, N+1):
                if arr[now][j] and not now_visited[j] and cnt + 1 > val_lst[j]:
                    s.append(j)
                    val_lst[j] = cnt + 1
                    now_visited[j] = True
                    break
            else:
                now_visited[s.pop()] = False
                cnt -= 2
        ans = max(ans, max(val_lst))
    print("#%d"%(tc), ans)