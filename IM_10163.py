N = int(input())
field = [[0] * 101 for _ in range(101)]

for num in range(1, N+1):
    j, i, W, H = map(int, input().split())
    for a in range(i, i + H):
        for b in range(j, j + W):
            field[a][b] = num

check = [0] * (N+1)
for a in range(101):
    for b in range(101):
        check[field[a][b]] += 1

for _ in range(1,N+1):
    print(check[_])