def check(y, x, val):   # 보드판의 (y, x)에 val값을 넣을 수 있는지 확인하는 함수
    if val in arr[y]:   # x축에 같은 값이 존재하는지 검토
        return False
    for i in range(9):  # y축에 같은 값이 존재하는지 검토
        if arr[i][x] == val:
            return False

    b = (y // 3) * 3    # (y, x)를 포함하는 작은 정사각형의 시작 y값
    a = (x // 3) * 3    # (y, x)를 포함하는 작은 정사각형의 시작 x값
    for i in range(3):  # 작은 정사각형 구역의 한 변의 길이가 3이므로 2중 for문 작성
        for j in range(3):  # x축 한 변의 길이 3에 대한 검토
            if arr[b+i][a+j] == val:    # 작은 정사각형 구역에 같은 값이 있는지 검토
                return False
    return True     # 스도쿠 조건을 모두 만족하였으면 True 반환


for tc in range(1, int(input()) + 1):
    N = int(input())    # 게임 수행 횟수
    arr = [list(map(int, input().split())) for _ in range(9)]   # 보드판 입력

    ans = 0
    for _ in range(N):
        y, x, val = map(int, input().split())
        if check(y, x, val):    # 스도쿠 조건을 만족하였다면
            arr[y][x] = val     # 보드판에 입력값 업데이트
            ans += 1            # 횟수 1 증가
        else:   # 만약 조건을 만족하지 못했다면
            for __ in range(_+1, N):    # 남은 input 자료 넘겨주고
                input()
            break   # for문 break

    print("#%d"%(tc), ans)