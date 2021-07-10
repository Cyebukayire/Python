weight = input("weight: ")
unit = raw_input("unit (L or K): ")
if unit.lower() == "l":
    Kilo = weight * 0.45
    print("Your weight in kilograms is: "+ str(Kilo))

elif unit.lower() == "k":
    pounds = weight/0.45
    print("You weight in pounds is: "+ str(pounds))

else:
    print("Your unit is not valid.\n")
