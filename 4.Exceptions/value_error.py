try:
    number = int(input("Enter number: "))
    print(number)

    income = 1000
    quotient = income/number
except NameError:
    print("Invalid input!")