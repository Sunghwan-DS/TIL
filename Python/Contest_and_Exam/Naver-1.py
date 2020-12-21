def solution(blocks):
    result = {}
    for idx, lst in enumerate(blocks):
        y = idx + 1
        x, val = lst
        result[(y, x)] = val
        for nx in range(x-1, -1, -1):
            result[(y, nx)] = result[(y-1, nx)] - result[(y, nx+1)]
        for nx in range(x+1, y):
            result[(y, nx)] = result[(y-1, nx-1)] - result[(y, nx-1)]

        answer = []
        for idx in range(len(blocks)):
            y = idx + 1
            for x in range(y):
                answer.append(result[(y, x)])

        return answer

ex1 = [[0, 50], [0, 22], [2, 10], [1, 4], [4, -13]]
print(solution(ex1))