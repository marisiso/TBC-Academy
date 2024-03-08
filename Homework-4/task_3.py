number = int(input('Please enter positive number below 1000: '))

divisors = []
if number <= 0 or number >= 1000:
    print('Number is not in specified range')
else:
    for i in range(1, number+1):
        if number % i == 0:
            divisors.append(i)
    print(divisors)
