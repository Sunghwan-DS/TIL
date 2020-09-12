def solution(num, cards):
    if cards[0] > num:
        return -1

    n_cards = []
    for n in cards:
        if n <= num:
            n_cards.append(n)
        else:
            break

    cards = n_cards
    cards.sort(reverse = True)

    def find_ans(res, answer, target):
        if res == target:
            return answer
        else:
            for n in cards:
                if res + n <= target:
                    find_ans(res + n, answer + 1, target)

        return answer

    return find_ans(0, 0, num)



sample1 = [8, [1, 4, 6]]
sample2 = [18, [1, 2, 5]]

print(solution(*sample1))