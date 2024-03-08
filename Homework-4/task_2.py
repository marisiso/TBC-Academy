import random

number = int(input('Please enter positive number below 30: '))
my_list = []
if number <= 0 or number >= 30:
    print('Number is not in specified range')
else:
    for _ in range(number):
        rand_number = random.randint(0, 1000)
        my_list.append(rand_number)
    print(max(my_list))
