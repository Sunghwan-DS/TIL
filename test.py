def backtracking(data,k):
    global maxsum, temp, start
    if k == 3:
        tempsum = temp % 10
        if tempsum > maxsum:
            maxsum = tempsum
        return

    for i in range(start, 5):
        if visited[i] == 0:
            visited[i] = 1
            temp += data[i]
            start += 1
            backtracking(data,k+1)
            visited[i] = 0
            temp -= data[i]
            start -= 1

N = int(input())
data = [list(map(int,input().split())) for _ in range(N)]
ans = [0] * N

for i in range(N):
    visited = [0] * 5
    maxsum = 0
    temp = 0
    start = 0
    backtracking(data[i],0)
    ans[i] = maxsum

num = 0

for i in range(N):
    if ans[i] >= ans[num]:
        num = i

print(num+1)