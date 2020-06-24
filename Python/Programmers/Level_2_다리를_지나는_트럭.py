def solution(bridge_length, weight, truck_weights):
    in_bridge = {}
    answer = 1
    now_weight = truck_weights[0]
    idx = 1
    in_bridge[0] = [1, truck_weights[0]]

    while in_bridge:
        del_lst = []
        for key in in_bridge:
            in_bridge[key][0] += 1
            if in_bridge[key][0] == bridge_length + 1:
                now_weight -= in_bridge[key][1]
                del_lst.append(key)

        for key in del_lst:
            del in_bridge[key]

        if idx < len(truck_weights):
            if now_weight + truck_weights[idx] <= weight:
                in_bridge[idx] = [1, truck_weights[idx]]
                now_weight += truck_weights[idx]
                idx += 1
        answer += 1
    return answer

print(solution(2, 10, [7,4,5,6]))
# print(solution(100, 100, [10]))
# print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))