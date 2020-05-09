def solution(expression):
    sequence = []
    number = ''
    for d in expression:
        if d in ('+', '-', '*'):
            sequence.append(int(number))
            number = ''
            sequence.append(d)
        else:
            number += d
    sequence.append(int(number))

    answer = 0

    cases = (('+', '-', '*'), ('+', '*', '-'), ('-', '+', '*'), ('-', '*', '+'), ('*', '+', '-'), ('*', '-', '+'))
    for case in cases:
        new_sequence = sequence[:]
        next_sequence = []
        cal_TF = False
        for sym in case:
            for data in new_sequence:

                if cal_TF:
                    if sym == '+':
                        next_sequence.append(prev_number + int(data))
                    elif sym == '-':
                        next_sequence.append(prev_number - int(data))
                    else:
                        next_sequence.append(prev_number * int(data))
                    cal_TF = False

                elif data != sym:
                    next_sequence.append(data)

                elif data == sym:
                    prev_number = next_sequence.pop()
                    cal_TF = True
            new_sequence = next_sequence[:]
            next_sequence = []
        answer = max(answer, abs(new_sequence[0]))

    return answer

print(solution("100-200*300-500+20"))