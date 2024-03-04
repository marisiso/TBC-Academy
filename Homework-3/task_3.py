import random

color = ['clubs', 'diamonds', 'hearts', 'spades']
number = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']

random_color = random.choice(color)
random_number = random.choice(number)

print(random_number, random_color)
