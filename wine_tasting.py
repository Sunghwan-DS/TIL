N = int(input())
wine = []
for _ in range(N):
    wine.append(int(input()))


if N == 1:
    print(wine[0])

elif N == 2:
    print(sum(wine))

else:
    drink_110 = wine[0] + wine[1]
    drink_101 = wine[0] + wine[2]
    drink_011 = wine[1] + wine[2]
    drink_100 = wine[0]
    drink_001 = wine[2]
    drink_010 = wine[1]

    for _ in range(3, N):
        drink_110, drink_101, drink_011, drink_100, drink_001, drink_010 = drink_011, max(drink_110, drink_010) + wine[_], max(drink_101, drink_001) + wine[_], drink_110, drink_100 + wine[_], max(drink_101, drink_001)

    print(max(drink_110, drink_101, drink_011, drink_110, drink_001, drink_010))