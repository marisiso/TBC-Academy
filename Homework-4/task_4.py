number = int(input('Please enter positive number from 0 to 21: '))

a = 0
b = 1
if number < 0 or number > 20:
    print('Number is not in specified range')
elif number == 0:
    print(a)
elif number == 1:
    print(b)
else:
    for _ in range(2, number + 1):
        c = a + b
        a = b
        b = c

    print(c)
