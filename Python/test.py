N = int(input())

row = [100] * N
check = [False] * (N+1)
result = 0



def checking(index, i):

    for j in range(index):
        if abs(row[j] - i) == abs(j - index):

            return True

def play(index, N):
    global result
    if index == N:
        result += 1
        return

    for i in range(1, N+1):
        if check[i]:
            continue
        elif checking(index, i):

            continue

        check[i] = True
        row[index] = i
        play(index+1, N)
        check[i] = False

play(0, N)
print(result)