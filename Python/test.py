N = int(input())
for tc in range(1, N+1):
    a, Hex = input().split()
    Hex = '0x'+Hex
    Bin = bin(int(Hex, 16))
    print("#%d"%(tc), '0' * (int(a) * 4 - len(Bin) + 2) + Bin[2:])