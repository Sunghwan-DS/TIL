N = int(input())
dice_original = []
for _ in range(N):
    dice_original.append(list(map(int,input().split())))

result = 0
for num in range(1,7):
    sum = 0
    for idx in range(N):
        dice = dice_original[idx][:]
        if dice.index(num) == 0:
            num = dice[5]
            dice[0] = 0
            dice[5] = 0
            sum += max(dice)
        elif dice.index(num) == 1:
            num = dice[3]
            dice[1] = 0
            dice[3] = 0
            sum += max(dice)
        elif dice.index(num) == 2:
            num = dice[4]
            dice[2] = 0
            dice[4] = 0
            sum += max(dice)
        elif dice.index(num) == 3:
            num = dice[1]
            dice[3] = 0
            dice[1] = 0
            sum += max(dice)
        elif dice.index(num) == 4:
            num = dice[2]
            dice[4] = 0
            dice[2] = 0
            sum += max(dice)
        elif dice.index(num) == 5:
            num = dice[0]
            dice[5] = 0
            dice[0] = 0
            sum += max(dice)

    if result < sum:
        result = sum

print(result)