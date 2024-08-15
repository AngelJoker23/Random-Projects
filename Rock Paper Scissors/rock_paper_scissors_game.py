import random
options = ["Rock", "Paper", "Scissors"]

machine = random.choice(options)

user = False
machine_score = 0
user_score = 0

while True:
    user = input("Rock, Paper, Scissors?").capitalize()

    if user == machine:
        print("Tie!")
    elif user == "Rock":
        if machine == "Paper":
            print("You Lose!", machine, "covers", user)
            machine_score += 1
        else:
            print("You Win!", user, "smashes", machine)
            user_score += 1
    elif user == "Paper":
        if machine == "Scissors":
            print("You Lose!", machine, "cut", user)
            machine_score += 1
        else:
            print("You Win!", user, "covers", machine)
            user_score += 1
    elif user == "Scissors":
        if machine == "Rock":
            print("You Lose!", machine, "smashes", user)
            machine_score += 1
        else:
            print("You Win!", user, "cut", machine)
            user_score += 1
    elif user == "End":
        print("Final Scores: ")
        print(f"Computer's Score is: {machine_score}")
        print(f"Your Score is: {user_score}")
        break
