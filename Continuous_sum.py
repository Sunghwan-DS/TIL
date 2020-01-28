n = int(input())
sequence = list(map(int, input().split()))
maximum = sequence[0]
if n == 1:
    print(maximum)
    exit()
no=sequence[0]
for _ in range(1, n):
    no = max(sequence[_], no+sequence[_])
    maximum = max(maximum, no)
print(maximum)