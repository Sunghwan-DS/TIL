N = int(input())
table = list(map(int, input().split()))
answer = [0] * N
max_num = table[0]
answer[0] = table[0]
i = 1
cnt = 1

for _ in range(1, N):
    if max_num > _ and not in