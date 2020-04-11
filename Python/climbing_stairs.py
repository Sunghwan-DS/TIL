n = int(input())

if n == 1:
    a = int(input())
    print(a)
    exit()

if n == 2:
    a = int(input())
    b = int(input())
    print(a+b)
    exit()

score = [0] * n
for _ in range(n):
    score[_] = int(input())

last1 = [0] * n
last2 = [0] * n
last1[0] = score[0]
last1[1] = score[0] + score[1]
last2[1] = score[1]
for i in range(2, n):
    last1[i] = last2[i-1] + score[i]
    last2[i] = max(last1[i-2] + score[i], last2[i-2] + score[i])

print(max(last1[n-1], last2[n-1]))