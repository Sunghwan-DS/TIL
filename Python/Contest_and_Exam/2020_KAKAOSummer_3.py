def solution(gems):
    record = {}
    start = 0
    end = 0
    length = 100000
    gems = [gems[0]] + gems
    for idx, jewelry in enumerate(gems):
        if jewelry not in record:
            record[jewelry] = idx
            end = idx
            answer = [start, end]
            length = end - start + 1
        else:
            if start == record[jewelry]:
                record[jewelry] = idx
                end = idx
                new_start = 100000
                for jewelry in record:
                    if record[jewelry] < new_start:
                        new_start = record[jewelry]
                start = new_start
                new_length = end - start + 1
                if new_length < length:
                    length = end - start + 1
                    answer = [start, end]
            else:
                record[jewelry] = idx

    if answer == [0, 0]:
        answer = [1, 1]
    return answer

print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))