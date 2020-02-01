B = int(input())
N = int(input())
distance = list(map(int,input().split()))   # N+1개의 자료
time = list(map(int,input().split()))      # N+1개의 자료

queue = [[0,B,0]]   # 시간, 갈수있는 거리, n번째 장소
fuel = 140
idx = 0
limit_time = [0] * (N+1)
n = 0
if fuel >= sum(distance):
    print("0")
    print("0")
    exit()
while queue:
    a = queue.pop(0)
    if a[0] > limit_time[n]:
        pass

    new_time = a[0] + time[idx]

    queue.append(a[0] + time[idx], B, n+1)
    if a[1] - distance[idx+1] <= 0:
        queue.append(a[0], a[1]-distance, idx+1)