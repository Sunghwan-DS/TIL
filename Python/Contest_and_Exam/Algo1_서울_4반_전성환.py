def move(num, idx):
    global new_arr
    if num > 0:
        if idx != 9:
            new_arr[idx + 1] += num
        else:
            new_arr[idx] -= num
    elif num < 0:
        if idx != 0:
            new_arr[idx - 1] += num
        else:
            new_arr[idx] -= num


for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int,input().split()))

    for i in range(N):
        new_arr = [0] * 10
        for idx, num in enumerate(arr):
            if abs(num) >= 10:
                move(-(abs(num)//2), idx)
                move(abs(num)//2, idx)

            else:
                move(num, idx)
        arr = new_arr[:]

    print("#%d"%(tc), *arr)