def just_brick(field, y, x):
    new_field = [field[__] for __ in range(H)]
    bomb = new_field[y][x]
    if bomb == 0:
        return
    new_field[y][x] = 0
    for __ in range(1, bomb):
        if x + __ > W-1:
            pass
        else:
            new_field = just_brick(new_field, y, x+__)
        if y + __ > H-1:
            pass
        else:
            new_field = just_brick(new_field, y+__, x)
        if x - __ < 0:
            pass
        else:
            new_field = just_brick(new_field, y, x-__)
        if y - __ < 0:
            pass
        else:
            new_field = just_brick(new_field, y -__, x)
    return new_field


def breaking(index, field, site):
    global result
    if index == N:
        cnt = 0
        for __ in range(H):
            cnt += field[__].count(0)
        if result > W * H -cnt:
            result = W * H - cnt
        # print(result)
        return

    new_field = [field[__] for __ in range(H)]

    for i in range(H):
        if new_field[i][site] != 0:
            bomb = new_field[i][site]
            new_field[i][site] = 0

            for __ in range(1, bomb):
                if site + __ > W-1:
                    pass
                else:
                    new_field = just_brick(new_field, i, site+__)
                if i + __ > H-1:
                    pass
                else:
                    new_field = just_brick(new_field, i+__, site)
                if site - __ < 0:
                    pass
                else:
                    new_field = just_brick(new_field, i, site-__)


            break

    







    for j in range(W):
        if new_field[H-1][j] == 0:
            pass
        else:
            breaking(index+1, new_field, j)






T = int(input())
for _ in range(T):
    N, W, H = map(int, input().split())
    field_original = [list(map(int, input().split())) for __ in range(H)]
    result = 100
    for j in range(10):
        if field_original[9][j] == 0:
            pass
        else:
            breaking(0, field_original, j)


    print("#%d %d"%(_ + 1, result))