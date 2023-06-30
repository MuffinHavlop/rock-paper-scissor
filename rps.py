import random

choices = ["Rock" , "Paper" , "Scissor"]
round = 0

while True:
    round += 1
    print(f"Round: {round}")
    cpu_choice = random.choice(choices)
    User_input = input("Enter your choice: ")
    User_input = User_input.lower()
    if cpu_choice == "Rock":
        if User_input == "paper":
            print("You won")
            break
        elif User_input == "scissor":
            print("You lost")
            continue
        elif User_input == "rock":
            print("Draw")
            continue
    if cpu_choice == "Paper":
        if User_input == "paper":
            print("Draw")
            continue
        elif User_input == "scissor":
            print("You won")
            break
        elif User_input == "rock":
            print("You lost")
            continue
    if cpu_choice == "Scissor":
        if User_input == "paper":
            print("You lost")
            continue
        elif User_input == "scissor":
            print("Draw")
            continue
        elif User_input == "rock":
            print("You won")
            break