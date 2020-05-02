import sys

def DFS(tree):
    stack = [0]
    n = 1
    for t in tree:
        if t == '0':
            stack.append(n)
            lst.append(n)
            n += 1
        else:
            k = stack.pop()
            lst.append(k)
            parents[k] = stack[-1]

input = sys.stdin.readline

N = int(input())
tree = input().strip()
X, Y = map(int, input().split())
lst = [0]
parents = [0 for _ in range(N+1)]
DFS(tree)
# print(lst)
print(parents)
print(lst)
X_parents = [lst[X]]
Y_parents = [lst[Y]]
print(X_parents, Y_parents)

while parents[lst[X]]:
    X_parents.append(parents[lst[X]])
    lst[X] = parents[lst[X]]
while parents[lst[Y]]:
    Y_parents.append(parents[lst[Y]])
    lst[Y] = parents[lst[Y]]

cut = 1
for x in X_parents:
    for y in Y_parents:
        if x == y:
            if cut < x:
                cut = x
TF = False
print(lst)
for i in range(2 * N):
    if lst[i] == cut:
        if not TF:
            TF = True
            dx = i
        else:
            dy = i
print(dx, dy)