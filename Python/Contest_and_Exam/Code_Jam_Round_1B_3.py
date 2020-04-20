for tc in range(1, int(input()) + 1):
    R, S = map(int,input().split())
    print("Case #%d:" % (tc), (R-1)*(S-1))

    for r in range(R, 1, -1):
        for cnt in range(1, S):
            front = r*(S-cnt)+(cnt-1)*(r-1)
            print(front, r*S-cnt-front)

# tc = 1
# for R in range(2, 5):
#     for S in range(2, 7):
#         print('R:',R, ',S:',S)
#         print("Case #%d:" % (tc), (R - 1) * (S - 1))
#         for r in range(R, 1, -1):
#             for cnt in range(1, S):
#                 front = r * (S - cnt) + (cnt - 1) * (r - 1)
#                 print(front, r * S - cnt - front)
#         tc += 1