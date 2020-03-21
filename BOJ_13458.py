# 2020.03.21
# 09:56 ~ 10:01
# 전탐
# 시간:728ms, 코드 길이:225B

N = int(input())
students = list(map(int,input().split()))
B, C = map(int,input().split())

ans = 0

for stu in students:
    stu -= B
    ans += 1
    if stu > 0:
        stu = stu + C - 1
        ans += stu // C

print(ans)