# hash 이용
def solution(k, room_number):
    hash = [[] for _ in range(100000)]
    dic = {}
    answer = []
    for num in room_number:
        while True:
            if num in hash[num%100000]:
                dic[num] += 1
                num += dic[num]
            else:
                dic[num] = 0
                hash[num%100000].append(num)
                answer.append(num)
                break
    return answer

# hash X
def solution(k, room_number):
    dic = {}
    answer = []
    for num in room_number:
        while True:
            if num in dic:
                dic[num] += 1
                num += dic[num]
            else:
                dic[num] = 0
                answer.append(num)
                break
    return answer

# 용준's
def solution(k, room_number):
    answer = []
    rooms = dict()
    for room in room_number:
        if not rooms.get(room):
            rooms[room] = room + 1
            answer.append(room)
        else:
            arrive = rooms.get(room)
            while rooms.get(arrive):
                rooms[arrive] = rooms[rooms[arrive]] + 1
                arrive = rooms.get(arrive)
            rooms[arrive] = arrive + 1
            rooms[room] = arrive
            answer.append(arrive)
    return answer