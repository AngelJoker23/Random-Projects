import random

# Range of a dice
min = 1
max = 6

# To loop the rolling through user input
Diceroll_again = "yes"

while Diceroll_again == "yes" or Diceroll_again == "y":
    print("Rolling your Dice....")
    print("The Values are: ")

    # Generate and Print 1st random value
print(random.randint(min, max))
print(random.randint(min, max))

# Generate and Print 2nd randome value
print(random.randint(min, max))
print(random.randint(min, max))

Diceroll_again = input("Do you want to roll the Dice Again?")
