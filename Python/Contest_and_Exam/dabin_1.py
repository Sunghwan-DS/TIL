def maxDifference(px):
    result = -1
    min_num = 100001
    max_num = -100001
    for num in px:
        if num > max_num:
            max_num = num
            result = max(result, max_num - min_num)
        if num < min_num:
            min_num = num
            max_num = -100001

    return result

print(maxDifference([7, 1, 5, 6]))
