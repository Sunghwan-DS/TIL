# 시간:276ms, 코드 길이:969B

def rotate(c):
    T, X, Y, Z, W = U, L, F, R, B
    if c == 'L':
        T, X, Y, Z, W = L, F, U, B, D
    if c == 'F':
        T, X, Y, Z, W = F, U, L, D, R
    if c == 'R':
        T, X, Y, Z, W = R, D, B, U, F
    if c == 'B':
        T, X, Y, Z, W = B, R, D, L, U
    if c == 'D':
        T, X, Y, Z, W = D, B, R, F, L

    p = T[:]
    for i in range(9):
        T[i] = p[q[i]]
    X[8], X[7], X[6], Y[6], Y[3], Y[0], Z[2], Z[5], Z[8], W[0], W[1], W[2] = Y[6], Y[3], Y[0], Z[2], Z[5], Z[8], W[0], W[1], W[2], X[8], X[7], X[6]


q = [6, 3, 0, 7, 4, 1, 8, 5, 2]
for _ in range(int(input())):
    U = ['w'] * 9
    D = ['y'] * 9
    F = ['r'] * 9
    B = ['o'] * 9
    L = ['g'] * 9
    R = ['b'] * 9
    n = int(input())
    data = list(input().split())
    for d in data:
        area, dir = d[0], d[1]
        rotate(area)
        if dir == '-':
            rotate(area)
            rotate(area)
    for i in range(3):
        print(''.join(U[i * 3:(i + 1) * 3]))