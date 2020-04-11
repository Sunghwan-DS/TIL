M, N = map(int,input().split())
K = int(input())

if K > M * N:
    print("0")
    exit()
    
j = 1
i = 0

p = 0
cnt = 0
t= 2*N + 2*M - 4
while K-t > 0:
    K -= t
    i+=1
    j+=1
    t -= 8
    cnt+=1
n = N - 2*cnt
m = M - 1 - 2*cnt

if K <= n:
    print("%d %d"%(j, i+K))
elif K<= n+m:
    print("%d %d"%(j+(K-n), i+n))
elif K <= n+m+n-1:
    print("%d %d"%(j+m, i+n-(K-n-m)))   
else:
    print("%d %d"%(j+m-(K-n-m-n+1), i+1))