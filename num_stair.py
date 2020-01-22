N = int(input())

end_num = [1] * 10
end_num[0] = 0
result = end_num[:]

for i in range(2, N+1):
    for _ in range(1,9):
        result[_] = end_num[_-1] % 1000000000 + end_num[_+1] % 1000000000
    result[0] = end_num[1] % 1000000000
    result[9] = end_num[8] % 1000000000
    end_num = result[:]

print(sum(result)%1000000000)