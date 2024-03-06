import random

players = int(input('Enter number of players: '))

if players < 0:
    print('You entered negative number of players!')
else:
    for i in range (players):
        die_1 = random.randint(1,6)
        die_2 = random.randint(1,6)
        print(die_1, die_2)