def QuickSort(lst):
    if len(lst) <= 1:
        return lst

    pivot = lst[len(lst)//2]
    lesser, equal, greater = [], [], []
    for num in lst:
        if num < pivot:
            lesser.append(num)
        elif num > pivot:
            greater.append(num)
        else:
            equal.append(num)
    return QuickSort(lesser) + equal + QuickSort(greater)

# print(QuickSort([4, 3, 17, 1, 2, 14, 9]))