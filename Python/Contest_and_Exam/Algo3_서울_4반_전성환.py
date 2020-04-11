def zip_img(N, y, x, ans):
    if N == 1:
        ans += arr[y][x]
        return ans
    stop = False
    for i in range(N):
        for j in range(N):
            if arr[y+i][x+j] != arr[y][x]:
                stop = True
                ans += 'x'
                ans = zip_img(N//2, y, x, ans)
                ans = zip_img(N//2, y, x+N//2, ans)
                ans = zip_img(N//2, y+N//2, x, ans)
                ans = zip_img(N//2, y+N//2, x+N//2, ans)
                break
        if stop:
            break
    else:
        ans += arr[y][x]
    return ans

N = int(input())
arr = [list(input().split()) for _ in range(N)]
print(zip_img(N, 0, 0, ''))