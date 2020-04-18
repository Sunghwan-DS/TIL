def make_password(J, M):
    global L, C
    if len(password) == L+1:
        if J >= 2 and M >= 1:
            answer = ''
            for idx in password[1:]:
                answer += data[idx]
            print(answer)
        return
    for idx in range(password[-1]+1, C):
        password.append(idx)
        if data[idx] in ('a', 'e', 'i', 'o', 'u'):
            make_password(J, M+1)
        else:
            make_password(J+1, M)
        password.pop()

L, C = map(int,input().split())
data = list(input().split())
data.sort()
password = [-1]
make_password(0, 0)