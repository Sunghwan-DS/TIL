from time import time
now = time()
tot = 0

for i in range(10000000):
    tot += 1
    tot += 1

print(tot, time() - now)