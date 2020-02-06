def find_route():




def go(d1, d2, d3, d4, idx, score):







dice = list(map(int,input().split()))

table1 = [0,  2,  4,  6,  8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40,  0,  0,  0,  0,  0]
table2 = [0,  0,  0,  0,  0, 10, 13, 16, 19, 25, 30, 35, 40,  0,  0,  0,  0,  0]
table3 = [0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 20, 22, 24, 25, 30, 35, 40,  0,  0,  0,  0,  0]
table4 = [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 30, 28, 27, 26, 25, 30, 35, 40,  0,  0,  0,  0,  0]

visited1 = [False] * len(table1)
visited2 = [False] * len(table2)
visited3 = [False] * len(table3)
visited4 = [False] * len(table4)

go(dice[0], 0, 0, 0, 1, table1[dice[0]])