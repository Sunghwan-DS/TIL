T = int(input())
for case in range(1, T+1):
    V, E = map(int,input().split())

    node = [[] for _ in range(V+1)]

    for i in range(E):
        s, e = map(int,input().split())
        node[s].append(e)


    S, G = map(int,input().split())
    TF = False
    s = [S]
    visited = [S]
    while s:
        current = s[-1]

        for i in node[current]:
            if i == G:
                TF = True
                break

            elif i not in visited:
                s.append(i)
                visited.append(i)
                break

        else:
            s.pop()

        if TF:
            break

    if TF:
        print("#%d"%(case), 1)
    else:
        print("#%d" % (case), 0)