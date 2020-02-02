B = int(input())
N = int(input())
distance = list(map(int,input().split()))   # N+1개의 자료
time = list(map(int,input().split()))      # N+1개의 자료

queue = [[0,B,0,[]]]   # 시간, 갈수있는 거리, n번째 장소, 들른 주유소

# print(time)
# print(distance)
result = []
limit_time = [[] for _ in range(N)]
if B >= sum(distance):
    print("0")
    print("0")
    exit()
while queue:
    a = queue.pop(0)
    if a[2] == N:
        if a[1] - distance[a[2]] >= 0:
            result.append(a[0])
            if a[0] == min(result):
                lst = a[3]
            continue
    # if a[0] > limit_time[n]:
    #     pass
    if a[1] - distance[a[2]] >= 0:
        queue.append([a[0], a[1]-distance[a[2]], a[2]+1, a[3]])
        next = a[3][:]
        next.append(a[2]+1)
        queue.append([a[0] + time[a[2]], B, a[2]+1, next])

print(min(result))
print(len(lst))
print(" ".join([str(i) for i in lst]))