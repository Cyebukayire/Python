import random


def roll():
    first_choice = random.randint(1, 6)
    second_choice = random.randint(1, 6)
    return first_choice, second_choice


class Dice:
    pass


dice1 = Dice()
print(roll())
