import time

lst = [i for i in range(10000, 0, -1)]
now = time.time()

new_list = sorted(lst)
print(lst)
print(new_list)
print(time.time() - now)