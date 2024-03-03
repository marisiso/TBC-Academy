import datetime

year = int(input('შეიყვანეთ თქვენი დაბადების წელი: '))
month = int(input('შეიყვანეთ თქვენი დაბადების თვე (ნომერი): '))
day = int(input('შეიყვანეთ თქვენი დაბადების რიცხვი: '))
birthday = datetime.datetime(year, month, day)

print('You were born on ', birthday.strftime("%A"))
