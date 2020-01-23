N = int(input())
people = list(map(int, input().split()))
people.insert(0, 0)
connection = [[]]
answer = 10000
for _ in range(N):
    a = list(map(int, input().split()))
    del a[0]
    connection.append(a)



def making_team(index, A, B):
    global answer
    if index == N:
        if B == []:
            return

        for i in A:
            TF = False
            for j in A:
                if j in connection[i]:
                    TF = True
                    break
                else:
                    pass
            if not TF:
                return

        for i in B:
            TF = False
            for j in B:
                if j in connection[i]:
                    TF = True
                    break
                else:
                    pass
            if not TF:
                return

        sumA = 0
        sumB = 0

        for i in A:
            sumA += people[i]
        for i in B:
            sumB += people[i]
        result = abs(sumA - sumB)

        if answer > result:
            answer = result

        return


    A_new = A[:]
    B_new = B[:]
    A_new.append(index+1)
    B_new.append(index+1)
    making_team(index+1, A_new, B)
    making_team(index+1, A, B_new)


making_team(1, [1], [])
if answer == 10000:
    print("-1")
    exit()
print(answer)