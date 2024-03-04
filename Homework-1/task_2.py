Name = input("Enter your name: ")
Year_born = int(input("Enter year you were born in: "))
Age = 2024 - Year_born

if Year_born > 2024:
    print('Year of birth can not be greater than 2024!')
else:
    print("Hi,", Name, "you are", Age, "years old")
