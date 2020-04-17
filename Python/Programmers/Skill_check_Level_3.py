# 편의점
def check(idx, money, seq, res, n):
    if res > n:
        return 0
    if res == n:
        return 1
    if idx == len(money):
        return 0
    if idx == len(money)-1:
        i = (n-res)//money[idx]
        seq[idx] = i
        cnt = check(idx+1, money, seq, res+i*money[idx], n)
        seq[idx] = 0
        return cnt
    cnt = 0
    for i in range(((n-res)//money[idx])+1):
        seq[idx] = i
        cnt += check(idx+1, money, seq, res+i*money[idx], n)
        seq[idx] = 0
    return cnt

def solution(n, money):
    money.sort(reverse = True)
    seq = [0] * len(money)
    answer = check(0, money, seq, 0, n) % 1000000007
    return answer

# 국가의 역할
def MergeSort(lst):
    if len(lst) == 1:
        return lst
    left = MergeSort(lst[:len(lst)//2])
    right = MergeSort(lst[len(lst)//2:])
    L, R = 0, 0
    sorted_list = []
    while L < len(left) and R < len(right):
        if left[L] < right[R]:
            sorted_list.append(left[L])
            L += 1
        elif left[L] > right[R]:
            sorted_list.append(right[R])
            R += 1
        else:
            sorted_list.append(left[L])
            L += 1
            R += 1

    if L == len(left):
        sorted_list.extend(right[R:len(right)])
    else:
        sorted_list.extend(left[L:len(left)])

    return sorted_list


def solution(budgets, M):
    plans = MergeSort(budgets)
    res = 0
    for idx, money in enumerate(plans):
        if res + money * (len(plans) - idx) > M:
            return (M - res) // (len(plans) - idx)
        else:
            res += money
    return money