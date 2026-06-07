import random
number_of_streaks = 0
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
logging.disable(logging.CRITICAL)
for experiment_number in range(10000):  # Run 10,000 experiments total.
    # Code that creates a list of 100 'heads' or 'tails' values
    total = []
    for i in range(100):
        total.append(random.choice(['T','H']))
    logging.debug(total)
    # Code that checks if there is a streak of 6 heads or tails in a row
    for i in range(len(total)):
        if total[i:i+6] in [['H','H','H','H','H','H'],['T','T','T','T','T','T']]:
            number_of_streaks += 1
            logging.debug([experiment_number, number_of_streaks])
print('Chance of streak: %s%%' % (number_of_streaks / 10000))