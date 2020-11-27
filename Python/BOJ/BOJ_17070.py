# 2020.11.27
# 16:07 ~ 16:37

N = int(input())
field = []
for _ in range(N):
    row = list(map(int, input().split()))
    field.append(row)

DP = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]
DP[0][1][0] = 1
for i in range(N):
    for j in range(1, N):
        if not field[i][j]:
            if j > 0:
                DP[i][j][0] += DP[i][j-1][0] + DP[i][j-1][1]
                if i > 0:
                    if not field[i-1][j] and not field[i][j-1]:
                        DP[i][j][1] += sum(DP[i-1][j-1])
            if i > 0:
                DP[i][j][2] += DP[i-1][j][1] + DP[i-1][j][2]

answer = sum(DP[N-1][N-1])
print(answer)