from cmath import log, log10, sqrt
from tokenize import Exponent


# for i in range(1, 11):
#     payout = 1 + i              # payout multiplier for crash game
#     winChance = 1/payout * .99              # probability of winning based on payout multiplier
#     print('Payout... x ' + str(payout) + "\t\tWin Chance... " + str(winChance * 100) + '%')               # prints payout multiplier & win rate



for i in range(1, 11):
    payout = 1 + i              # payout multiplier for crash game
    winChance = 1/payout * .99              # probability of winning based on payout multiplier
    expectedPayout = payout * winChance
    print('Payout... x ' + str(payout) + "\t\tWin Chance... " + str(round(winChance * 100, 1)) + '%' + "\t\tExpected Payout... " + str(round(expectedPayout * 100, 2)) + '%')               # prints payout multiplier & win rate



print('\n')
