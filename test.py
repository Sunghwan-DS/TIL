for tc in range(1, int(input()) + 1):
    val = round(pow(int(input()), 1/3), 2)
    if val != int(val):
        val = -1
    print("#%d"%(tc), int(val))