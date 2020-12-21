import requests
from collections import deque

token = "177ab1cc65d027ac7275cc716f0f0a93" # x_auth_token

URL = "https://pegkq2svv6.execute-api.ap-northeast-2.amazonaws.com/prod/users"

def start(num):
    URI = URL + '/' + 'start'
    return requests.post(URI, headers={"X-Auth-Token": token}, json={"problem": num}).json()

    # {
    #   "auth_key": "1fd74321-d314-4885-b5ae-3e72126e75cc",
    #   "problem": 1,
    #   "time": 0
    # }

problem_num = 1
if problem_num == 1:
    N = 5
    # 분당 2건, 자전거 100대 & 초기 4대씩, 트럭 5대
elif problem_num == 2:
    N = 60
    # 분당 15건, 자전거 10,800대 & 초기 3대씩, 트럭 10대

start = start(problem_num)
print(start)
auth_key = start["auth_key"]
problem = start["problem"]
time = start["time"]


def getlocations():
    URI = URL + '/' + 'locations'
    return requests.get(URI, headers={"Authorization": auth_key}).json()

    # {
    #   "locations": [
    #     { "id": 0, "located_bikes_count": 3 },
    #     { "id": 1, "located_bikes_count": 3 },
    #     ...
    #   ]
    # }


def gettrucks():
    URI = URL + '/' + 'trucks'
    return requests.get(URI, headers={"Authorization": auth_key}).json()

    # {
    #     "trucks": [
    #         { "id": 0, "location_id": 0, "loaded_bikes_count": 0 },
    #         { "id": 1, "location_id": 0, "loaded_bikes_count": 0 },
    #         ...
    #     ]
    # }


def getsimulate(cmds):
    URI = URL + '/' + 'simulate'
    return requests.put(URI, headers={"Authorization": auth_key}, json={"commands": cmds}).json()

    # 0: 6초간 아무것도 하지 않음
    # 1: 위로 한 칸 이동
    # 2: 오른쪽으로 한 칸 이동
    # 3: 아래로 한 칸 이동
    # 4: 왼쪽으로 한 칸 이동
    # 5: 자전거 상차
    # 6: 자전거 하차
    #
    # 예를 들어, `{ "truck_id": 0, "command": [2, 5, 4, 1, 6] }`으로 명령을 하면 ID가 0인 트럭은 아래와 같이 운행한다.
    # 1) 오른쪽으로 한 칸 이동
    # 2) 자전거 1대 상차
    # 3) 왼쪽으로 한 칸 이동
    # 4) 위로 한 칸 이동
    # 5) 자전거 1대 하차

    # cmds = [
    #          { "truck_id": 0, "command": [2, 5, 4, 1, 6] }
    #          ...
    #        ]

    # {
    #   "status": "ready",
    #   "time": 1,
    #   "failed_requests_count": 5,
    #   "distance": 1.2,
    # }


def getscore():
    URI = URL + '/' + 'score'
    return requests.get(URI, headers={"Authorization": auth_key}).json()


def id_to_yx(id):
    x = id // N
    y = (N - 1) - (id % N)
    return y, x

# 위1, 오른쪽2, 아래3, 왼쪽4
dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)

def getcmd(tid, truck_bikes):
    def id_to_yx(id):
        x = id // N
        y = (N - 1) - (id % N)
        return y, x
    cmd = []
    cnt = truck_bikes
    # 상차5, 하차6
    ty, tx = id_to_yx(tid)
    # command가 10개 모일때까진 반복할 것이다.
    while True:
        max_effect = 0
        target_id = -1
        target_y = -1
        target_x = -1
        action = [0, 0]

        for id in range(N ** 2):
            lo_cnt = bikes[id]
            ly, lx = id_to_yx(id)

            distance = abs(ty - ly) + abs(tx - lx)
            if lo_cnt > case:
                lo_minus = lo_cnt - case
                car_plus = 10 - cnt
                work = min(lo_minus, car_plus)
                if work + distance == 0:
                    continue
                effect = (work / (work + distance))
                # print(id, effect, work, work + distance)
                if effect > max_effect:
                    if id not in check:
                        target_id = id
                        target_y = ly
                        target_x = lx
                        max_effect = effect
                        action = [5, work]

            elif lo_cnt < case:
                lo_plus = case - lo_cnt
                car_minus = cnt
                work = min(lo_plus, car_minus)
                if work + distance == 0:
                    continue
                effect = (work / (work + distance))
                # print(id, effect, work, work + distance)
                if effect > max_effect:
                    if id not in check:
                        target_id = id
                        target_y = ly
                        target_x = lx
                        max_effect = effect
                        action = [6, work]

        if not max_effect:
            while len(cmd) < 10:
                cmd.append(0)
            return cmd
        else:
            check[target_id] = 1

        if target_y > ty:
            for i in range(target_y - ty):
                if len(cmd) == 10:
                    return cmd
                cmd.append(3)
        elif target_y < ty:
            for i in range(ty - target_y):
                if len(cmd) == 10:
                    return cmd
                cmd.append(1)
        if target_x > tx:
            for i in range(target_x - tx):
                if len(cmd) == 10:
                    return cmd
                cmd.append(2)
        if target_x < tx:
            for i in range(tx - target_x):
                if len(cmd) == 10:
                    return cmd
                cmd.append(4)

        for i in range(action[1]):
            if len(cmd) == 10:
                return cmd
            if action[0] == 5:
                cnt += 1
            else:
                cnt -= 1
            cmd.append(action[0])

        if len(cmd) == 10:
            return cmd
        ty = target_y
        tx = target_x


while True:
    locations = getlocations()["locations"]
    bikes = {}
    total_bikes = 0
    for location in locations:
        bikes[location["id"]] = location["located_bikes_count"]
        total_bikes += location["located_bikes_count"]

    check = {}
    cmds = []
    trucks = gettrucks()["trucks"]
    # print(trucks)
    for truck in trucks:
        total_bikes += truck["loaded_bikes_count"]
    case = total_bikes // (N ** 2)
    print("조건", case, "자전거 수:", bikes)

    for truck in trucks:
        cmd = (getcmd(truck["location_id"], truck["loaded_bikes_count"]))
        cmds.append({"truck_id": truck["id"], "command": cmd})

    print("명령어:", cmds)
    # print("check:", check)
    result = getsimulate(cmds)
    # print(result)
    if result["status"] == "finished":
        print(result)
        score = getscore()
        print(score)
        break
