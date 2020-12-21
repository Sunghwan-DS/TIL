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
    case = 4
    # 분당 2건, 자전거 100대 & 초기 4대씩, 트럭 5대
elif problem_num == 2:
    N = 60
    case = 3
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

def BFS(y, x, truck_bikes):
    cmd = []
    cnt = truck_bikes
    # 상차5, 하차6

    # command가 10개 모일때까진 반복할 것이다.
    while True:
        if len(cmd) == 10:
            return cmd

        # 현재 내 위치에서 상차가 가능하다면
        if mymap[y][x] > case:
            if cnt < 10:
                cmd.append(5)
                cnt += 1
                continue
        # 현재 내 위치에서 하차가 가능하다면
        elif mymap[y][x] < case:
            if cnt > 0:
                cmd.append(6)
                cnt -= 1
                continue
        break

    while True:
        max_effect = 0
        target_y = -1
        target_x = -1
        action = [0, 0]

        for ny in range(N):
            for nx in range(N):
                lo_cnt = mymap[ny][nx]
                distance = abs(y - ny) + abs(x - nx)
                if distance == 0:
                    continue
                if lo_cnt > case:
                    lo_minus = lo_cnt - case
                    car_plus = 10 - cnt
                    work = min(lo_minus, car_plus)
                    effect = (work / (work + distance))
                    if effect > max_effect:
                        if (target_y, target_x) not in check:
                            target_y = ny
                            target_x = nx
                            max_effect = effect
                            action = [5, work]

                elif lo_cnt < case:
                    lo_plus = case - lo_cnt
                    car_minus = cnt
                    work = min(lo_plus, car_minus)
                    effect = (work / (work + distance))
                    if effect > max_effect:
                        if (target_y, target_x) not in check:
                            target_y = ny
                            target_x = nx
                            max_effect = effect
                            action = [6, work]

        if not max_effect:
            while len(cmd) < 10:
                cmd.append(0)
            return cmd

        if target_y > y:
            for i in range(target_y - y):
                if len(cmd) == 10:
                    return cmd
                cmd.append(3)
        elif target_y < y:
            for i in range(y - target_y):
                if len(cmd) == 10:
                    return cmd
                cmd.append(1)
        if target_x > x:
            for i in range(target_x - x):
                if len(cmd) == 10:
                    return cmd
                cmd.append(2)
        if target_x < x:
            for i in range(x - target_x):
                if len(cmd) == 10:
                    return cmd
                cmd.append(4)

        for i in range(action[1]):
            if len(cmd) == 10:
                return cmd
            cmd.append(action[0])

        if len(cmd) == 10:
            return cmd
        y = target_y
        x = target_x


while True:
    locations = getlocations()["locations"]
    mymap = [[0] * N for _ in range(N)]
    for location in locations:
        y, x = id_to_yx(location["id"])
        mymap[y][x] = location["located_bikes_count"]
    print(location)
    for i in range(N):
        print(*mymap[i])

    check = {}
    cmds = []
    trucks = gettrucks()["trucks"]
    # print(trucks)
    for truck in trucks:
        y, x = id_to_yx(truck["location_id"])
        cmd = (BFS(y, x, truck["loaded_bikes_count"]))
        cmds.append({"truck_id": truck["id"], "command": cmd})
    print(cmds)

    result = getsimulate(cmds)
    # print(result)
    if result["status"] == "finished":
        print(result)
        score = getscore()
        print(score)
        break
