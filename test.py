num = int(input())
data = [[i for i in map(int,input().split())] for j in range(num)]  # num 개의 색종이 자료
mymap = [[0]*101 for i in range(101)]   # 101*101
for i in range(num):
    for j in range(data[i][0], data[i][0] + data[i][2]):
        for k in range(data[i][1], data[i][1] + data[i][3]):
            mymap[k][j] += 1

ans = [0] * num
for i in range(num):
    for j in range(data[i][0], data[i][0] + data[i][2]):
        for k in range(data[i][1],data[i][1] +data[i][3]):
            if mymap[k][j] in range(i+2):
                ans[i] += 1

for i in range(num):
    print(ans[i])