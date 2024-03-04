Name = input("Enter your name: ")
Surname = input("Enter your surname: ")
Age = int(input("Enter your age: "))

if Age < 0:
    print("Age can not be negative!")
else:
    print("Hi,", Name, Surname, ",you are", Age, "years old")
