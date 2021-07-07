guess_count = 0
guess__limit = 3
secret = 9
while guess_count < guess__limit:
    # guess = int(input("Enter Guess Number: "))
    guess = input("Enter number: ")
    if guess == secret:
        print("You won!")
        break
    else:
        print("You lose!")
    guess_count = guess_count + 1
# 0788311606