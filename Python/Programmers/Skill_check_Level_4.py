# def solution(n, cores):
#     if n <= len(cores):
#         answer = n
#     else:
#         n -= len(cores)
#         time = 0
#         while n != 0:
#             time += 1
#             for idx, num in enumerate(cores):
#                 if time % num == 0:
#                     n -= 1
#                     if n == 0:
#                         answer = idx + 1
#                         break
#     return answer
#
# print(solution(6, [1,2,3]))



def solution(words):
    record = {}
    answer = 0
    for word in words:
        for idx in range(len(word), 0, -1):
            check = word[:idx]
            if check in record:
                if record[check] > 1:
                    answer += min(idx+1, len(word))
                    print("break 추가", idx+1)
                    break
                else:
                    record[check] += 1
                    answer += 2
            else:
                record[check] = 1
        else:
            if record[word[:1]] <= 2:
                answer += 1
        print(record)
        print(answer)
    return answer

print(solution(['word', 'war', 'warrior', 'world']))