def calc(prob_win, money):
    
    prob_lose = 1 - prob_win
    prob_win_round = prob_win
    
    bet = 1
    bet_curr = 1
    money_left = money - bet_curr
    num_rounds = 1
    print("current round, current bet, total bet, money left, prob of winning this round")
    print(num_rounds, bet_curr, bet, money_left, prob_win_round)
    
    while bet <= money_left:
        bet_curr = bet_curr * 2
        bet = bet + bet_curr
        money_left = money_left - bet_curr
        prob_win_round = pow(prob_lose, num_rounds) * prob_win
        num_rounds += 1
        print(num_rounds, bet_curr, bet, money_left, "{0:.4f}".format(prob_win_round))
    
    print("num of rounds = ", num_rounds)

calc(0.5, 100)
calc(0.4, 100)
