N = int(input())
arr = [set() for _ in range(51)]
for i in range(N):
    c = input()
    arr[len(c)].add(c)

for i in range(1, 51):
    if arr[i]:
        for word in sorted(list(arr[i])):
            print(word)