def cal_key(num):
    return num % 200000

def solution(k, room_number):
    hash = [[] for _ in range(200000)]
    answer = []
    for num in room_number:
        while True:
            if num in hash[cal_key(num)]:
                num += 1
            else:
                hash[cal_key(num)].append(num)
                answer.append(num)
                break
    return answer


print(solution(1000000000000, [1]*10000))