N = int(input())
for _ in range(N):
    data_A = list(map(int,input().split()))
    data_B = list(map(int,input().split()))
    table_A = [0,0,0,0,0]
    table_B = [0,0,0,0,0]
    for i in data_A[1:]:
        table_A[i] += 1
    for j in data_B[1:]:
        table_B[j] += 1

    for num in range(4, 0, -1):
        if table_A[num] > table_B[num]:
            print("A")
            break
        elif table_A[num] < table_B[num]:
            print("B")
            break
    else:
        print("D")