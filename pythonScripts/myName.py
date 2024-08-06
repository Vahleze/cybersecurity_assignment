import random
number_to_guess = random.randint(1, 4)

pick_a_number = int(input("Guess a number between 1 and 4 "))
if pick_a_number == number_to_guess:
    print("You win")
else:
    print("Try again!") 