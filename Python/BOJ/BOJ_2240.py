T, W = map(int, input().split())
DP1 = [[-1] * T for i in range(W+1)]
DP2 = [[-1] * T for i in range(W+1)]

jadu = input()
if jadu == '1':
    DP1[0][0] = 1
    DP2[0][0] = 0
else:
    DP2[1][0] = 1
    DP1[0][0] = 0

for t in range(1, T):
    jadu = input()
    if jadu == '1':
        for w in range(W+1):
            if DP1[w][t-1] >= 0:
                DP1[w][t] = DP1[w][t-1] + 1
            if w-1 >= 0 and DP2[w-1][t-1] >= 0:
                DP1[w][t] = max(DP1[w][t], DP2[w-1][t-1] + 1)
            if DP2[w][t-1] >= 0:
                DP2[w][t] = DP2[w][t-1]
    else:
        for w in range(W + 1):
            if DP2[w][t - 1] >= 0:
                DP2[w][t] = DP2[w][t - 1] + 1
            if w - 1 >= 0 and DP1[w-1][t-1] >= 0:
                DP2[w][t] = max(DP2[w][t], DP1[w-1][t-1] + 1)
            if DP1[w][t - 1] >= 0:
                DP1[w][t] = DP1[w][t - 1]

# for i in range(W+1):
#     print(DP1[i])
# print()
# for i in range(W+1):
#     print(DP2[i])
# print()

ans = 0
for i in range(W+1):
    ans = max(ans, DP1[i][T-1], DP2[i][T-1])
print(ans)