n = int(input())
ch = input()
x, y = map(int,input().split())

stack = []
tree = [0]*999999
tree2 = [0]

a=0
s=1
try:
    for i in ch:
        if i == '0':
            a+=1
            if tree[s]==0:
                tree[s]=a
            else:
                s+=1
                tree[s]=a
            s*=2
            tree2.append(a)
            stack.append(a)
        else:
            s=s//2
            b=stack.pop()
            tree2.append(b)

    x=tree2[x]
    y=tree2[y]
    x=tree.index(x)
    y=tree.index(y)
    X=[]

    while x>0:
        X.append(x)
        x//=2

    Y=[]
    while y>0:
        Y.append(y)
        y//=2

    croot=0
    for i in X:
        for j in Y:
            if i==j:
                croot=i
                break
        if croot:
            break
    croot=tree[croot]
    ans=[]

    ans1=tree2.index(croot)
except ValueError:
    print("Error")
    exit()
ans.append(ans1)
try:
    ans.append(ans1+1+tree2[ans1+1:].index(croot))
except:
    pass
print(*ans)