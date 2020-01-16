import numpy as np

start = 6000

budget = start

for __ in range(20):

    current = budget

    cont = True

    if budget < start - 1000:
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

            if budget < current - 2000:# and len(labby_line) > 4:
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