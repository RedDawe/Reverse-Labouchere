import numpy as np

start = 6000
absolute_stop_loss = 1000
daily_stop_loss = 200
playing_days = 2000

budget = start

for __ in range(playing_days):

    current = budget

    cont = True

    if budget < start - absolute_stop_loss:
        break

    for _ in range(11):

        if not cont:
            break

        labby_line = [5, 5, 5, 5]

        while labby_line:
            if len(labby_line) > 1:
                bet = labby_line[0] + labby_line[-1]
            else:
                bet = labby_line[0]

            if budget < current - daily_stop_loss:# and len(labby_line) > 4:
                cont = False
                break

            if bet > budget:
                cont = False
                break

            if np.random.rand() >= 0.5:
            #if np.random.rand() > 0.5:
                budget += bet
                if len(labby_line) > 1:
                    labby_line.pop(0)
                    labby_line.pop(-1)
                else:
                    labby_line.pop(0)
            else:
                labby_line.append(bet)
                budget -= bet

print((budget - start)*0.9 + start, budget > start)