try:
    number = int(input("Enter number: "))
    print(number)

    income = 1000
    quotient = income/number
    print(quotient)
except NameError:
    print("Error: Invalid input!")
except ZeroDivisionError:
    print("Error: Module by zero!")

