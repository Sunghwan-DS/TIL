for T in range(1, int(input()) + 1):
    data = list(map(int,list(input())))
    ans = ''
    ans += data[0] * '(' + str(data[0])
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            ans += (data[i] - data[i-1]) * '(' + str(data[i])
        elif data[i] < data[i-1]:
            ans += (data[i-1] - data[i]) * ')' + str(data[i])
        else:
            ans += str(data[i])
    ans += data[len(data)-1] * ')'
    print("Case #%d:"%(T), ans)
