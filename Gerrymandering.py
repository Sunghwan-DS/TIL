N = int(input())
people = list(map(int, input().split()))
people.insert(0, 0)
connection = [[]]
answer = 1000
for _ in range(N):
    a = list(map(int, input().split()))
    del a[0]
    connection.append(a)


def checking(team):
    check_list = [team[0]]
    for _ in range(len(team)-1):
        for i in check_list:
            for j in connection[i]:
                if j not in check_list and j in team:
                    check_list.append(j)
    if len(check_list) == len(team):
        return True
    else:
        return False


def making_team(index, A, B):
    global answer
    if index == N:
        if B == []:
            return

        if not checking(A):
            return

        if not checking(B):
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
if answer == 1000:
    print("-1")
    exit()
print(answer)