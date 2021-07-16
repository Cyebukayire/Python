import random


class Dice():

    def roll(self):
        first_choice = random.randint(1, 6)
        second_choice = random.randint(1, 6)
        return first_choice, second_choice 



dice1 = Dice()
print(dice1.roll())
