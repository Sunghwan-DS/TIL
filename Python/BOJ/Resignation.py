def go(index, money):
    global result
    if index == N:
        if result < money:
            result = money
        return
    if index + schedul[index][0] <= N:
        go(index + schedul[index][0], money + schedul[index][1])
    
    go(index+1, money)


N = int(input())
schedul = []
result = 0
for _ in range(N):
    schedul.append(list(map(int,input().split())))


go(0, 0)
print(result)