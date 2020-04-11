def MergeSort(lst):
    if len(lst) == 1:
        return lst

    left = MergeSort(lst[:len(lst)//2])
    right = MergeSort(lst[len(lst)//2:])

    L, R = 0, 0
    sorted_list = []
    while L < len(left) and R < len(right):
        if left[L] <= right[R]:
            sorted_list.append(left[L])
            L += 1
        else:
            sorted_list.append(right[R])
            R += 1

    if L == len(left):
        sorted_list.extend(right[R:len(right)])
    else:
        sorted_list.extend(left[L:len(left)])

    return sorted_list

print(MergeSort([8, 3, 5, 1, 2, 10, 6, 3, 2, 5, 1]))