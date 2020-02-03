B = int(input())
N = int(input())
distance = list(map(int,input().split()))   # N+1개의 자료
time = list(map(int,input().split()))      # N+1개의 자료

queue = [[B,0,[]]]   # 갈수있는 거리, n번째 장소, 들른 주유소

result = []
if B >= sum(distance):
    print("0")
    print("0")
    print("")
    exit()

while queue:
    size = len(queue)
    test = []
    for i in range(size):
        a = queue.pop(0)
        if a[1] == N:
            if a[0] - distance[a[1]] >= 0:
                t = 0
                for __ in a[2]:
                    t += time[__-1]
                result.append(t)
                if t == min(result):
                    lst = a[2]
                continue

        if a[0] - distance[a[1]] >= 0:
            queue.append([a[0]-distance[a[1]], a[1]+1, a[2]])
            next = a[2][:]
            next.append(a[1]+1)
            test.append([B, a[1]+1, next])

    t_lst = []
    for j in test:
        t = 0
        for __ in j[2]:
            t += time[__ - 1]
            t_lst.append(t)
    if t_lst == []:
        break
    b = t_lst.index(min(t_lst))
    queue.append(test[b])

print(min(result))
print(len(lst))
print(" ".join([str(i) for i in lst]))