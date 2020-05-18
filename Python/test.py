import time
now = time.time()
num = 0

for _ in range(10**8):
    num += 1
    num += 1
    num += 1
    num += 1
    num += 1
    num += 1
    num += 1
    num += 1
    num += 1
    num += 1

print(num)
print(time.time() - now)