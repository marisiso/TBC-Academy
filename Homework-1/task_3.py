import math
a = int(input("Enter triangle side a = "))
b = int(input("Enter triangle side b = "))
c = int(input("Enter triangle side c = "))
per = a+b+c
s = per/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))

if a < 0 or b < 0 or c < 0:
    print("Side length can not be negative!")
else:
    print("Perimeter of triangle is", per)
    print("Area of triangle is", area)
