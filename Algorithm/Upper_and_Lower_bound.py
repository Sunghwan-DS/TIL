def lower_bound(lst, target):
    low = 0
    high = len(lst) - 1

    while low < high:
        m = (low + high) // 2
        if lst[m] < target:
            low = m + 1
        else:
            high = m
    if lst[high] < target:
        return len(lst)
    return high

def upper_bound(lst, target):
    low = 0
    high = len(lst)

    while low < high:
        m = (low + high) // 2
        if lst[m] <= target:
            low = m + 1
        else:
            high = m
    high -= 1
    if lst[high] > target:
        return 'no'
    return high

lst = [5, 5, 5, 6]
print(len(lst) - lower_bound(lst, 7))
# print(upper_bound(lst, 1))