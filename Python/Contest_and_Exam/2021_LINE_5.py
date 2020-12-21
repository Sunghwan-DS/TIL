# 11:24 ~ 12:06

def solution(cards):
    global idx
    def end_game(idx, end):
        if idx == end:
            return True
        else:
            return False

    idx = 0
    end = len(cards)

    def cal_sum(cal_cards):
        cal_cards.sort(reverse=True)
        res = 0
        for card in cal_cards:
            if card in [11, 12, 13]:
                res += 10
            elif card == 1:
                if res + 11 <= 21:
                    res += 11
                else:
                    res += 1
            else:
                res += card
        return res

    def game():
        global idx
        end = len(cards)

        # 내가 카드 1장 받기
        I = [cards[idx]]
        idx += 1

        # 딜러가 카드 1장 받기
        if end_game(idx, end):
            return 0
        dealer = [cards[idx]]
        idx += 1

        # 내가 카드 1장 받기
        if end_game(idx, end):
            return 0
        I.append(cards[idx])
        idx += 1

        # 딜러가 카드 1장 받기
        if end_game(idx, end):
            return 0
        dealer_open = cards[idx]
        dealer.append(dealer_open)
        idx += 1

        # 내가 블랙잭이면
        if cal_sum(I) == 21:
            if cal_sum(dealer) == 21:
                return 0
            else:
                return 3
        # 딜러가 블랙잭이면
        if cal_sum(dealer) == 21:
            return -2

        # 딜러 카드가 1이나 7 이상이면
        if dealer_open == 1 or dealer_open >= 7:
            # 내 카드 합이 17 이상이 되도록 만든다
            while cal_sum(I) < 17:
                if end_game(idx, end):
                    return 0
                I.append(cards[idx])
                idx += 1
            if cal_sum(I) > 21:
                return -2

        # 딜러 카드가 4, 5, 6 이면
        elif dealer_open in [4, 5, 6]:
            pass

        # 딜러 카드가 2, 3 이면
        elif dealer_open in [2, 3]:
            while cal_sum(I) < 12:
                if end_game(idx, end):
                    return 0
                I.append(cards[idx])
                idx += 1
            if cal_sum(I) > 21:
                return -2

        # 딜러의 카드 추가 차례
        while cal_sum(dealer) < 17:
            if end_game(idx, end):
                return 0
            dealer.append(cards[idx])
            idx += 1
            if cal_sum(dealer) > 21:
                return 2

        cal_I = cal_sum(I)
        cal_dealer = cal_sum(dealer)
        if cal_I > cal_dealer:
            if cal_I == 21:
                return 3
            else:
                return 2

        elif cal_I < cal_dealer:
            return -2

        else:
            return 0

    answer = 0
    while idx < end:
        answer += game()

    return answer


ex1 = [12, 7, 11, 6, 2, 12] # ans = 2
ex2 = [1, 4, 10, 6, 9, 1, 8, 13] # ans = 1
ex3 = [10, 13, 10, 1, 2, 3, 4, 5, 6, 2]	 # ans = -2
ex4 = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3] # ans = -2

print(solution(ex1))