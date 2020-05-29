def DFS(idx, sum):

    global ans

    if idx == min(N, M):  # 사탕이 사람수보다 적다면, 사람수와 사탕수중 작은 값이 DFS깊이
        ans = max(ans, sum) # 최대값으로 교체해주고 return합니다.
        return

    DFS(idx + 1, sum)   # 아니라면
    for num in range(1, M+1):   # 사탕 종류인 1부터 M까지!

        if not Vst[num] and num not in Stack[idx]: # num사탕이 없고, idx번째 아이가 num 사탕이 없으면
            Vst[num] = True     # num 종류 사탕을 준것으로 체크
            DFS(idx + 1, sum + 1)   # 다음 아이에게 사탕을 주기 위해 다음 재귀로 넘어가는 부분
            Vst[num] = False    # 백트레킹을 위해 num 사탕의 visited 초기화


T = int(input())
for TC in range(1, T + 1):

    N, M = map(int, input().split())
    Vst = [False] * (M + 1)     # 여유분 사탕 중 이미 줘버린 종류를 확인하기 위한 리스트
    Stack = []     # 아이들이 가지고 있는 사탕을 기록해둘 리스트
    sum = 0    # 사탕을 나눠주기 전 아이들이 이미 가지고 있는 종류들의 합

    for i in range(N):
        data = list(map(int, input().split()))  # 데이터 입력
        data.pop(0) # 맨 앞의 사탕 개수 제거
        data_set = set(data)    # set을 이용하여 중복 제거
        sum += len(data_set)    # 사탕을 나눠주기 전 값을 계산하기 위해 반복문에서 더해준다
        Stack.append(data_set)  # stack에 i번째 아이가 가진 사탕 종류 기록

    ans = 0
    DFS(0, sum)
    print("#%d"%(TC), ans)