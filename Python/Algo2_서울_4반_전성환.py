def DFS(idx, res):  # DFS 백트레킹으로 문제를 해결
    global ans
    if idx == min_val:  # 사탕이 사람수보다 적으면 앞사람부터 나누어주기 때문에 DFS의 최대깊이는 사람 수 혹은 사탕 수 중 작은 값이다
        ans = max(ans, res) # 전역변수 설정을 해준 ans에 최대값 업데이트
        return

    DFS(idx + 1, res)   # 사탕을 주지 않고 다음 아이로 넘어가기 (위에서 min_val을 이용해 사탕 수와 사람 수 중 작은 값까지만 재귀가 돌아가므로 문제 조건과 상관없다)
    for num in range(1, M+1):   # 사탕 종류인 1부터 M까지 반복문
        if not visited[num] and num not in record[idx]: # num이라는 사탕을 준적이 없으며, idx번째 아이가 num 사탕을 가지고 있지 않으면
            visited[num] = True     # num이라는 종류의 사탕을 이미 주었다고 체크
            DFS(idx + 1, res + 1)   # 다음 아이에게 사탕을 주기 위해 다음 재귀로 넘어가는 부분
            visited[num] = False    # 백트레킹을 위해 num 사탕의 visited 초기화


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    min_val = min(N, M)     # 사탕 수와 사람 수 중 작은 값이 재귀 깊이가 되므로 이를 이용하기 위한 값
    visited = [False] * (M + 1)     # 여유분 사탕 중 이미 줘버린 종류를 확인하기 위한 리스트
    record = []     # 아이들이 가지고 있는 사탕을 기록해둘 리스트
    base = 0    # 사탕을 나눠주기 전 아이들이 이미 가지고 있는 종류들의 합
    for _ in range(N):
        tmp = set(list(map(int, input().split()))[1:])  # 맨 앞 값은 사탕의 개수이므로 이를 제외한 부분을 set으로 저장
        base += len(tmp)    # 사탕을 나눠주기 전 값을 계산하기 위해 반복문에서 더해준다
        record.append(tmp)  # record에 _번째 아이가 가진 사탕 종류 기록

    ans = 0
    DFS(0, base)
    print("#%d"%(tc), ans)