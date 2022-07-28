import random


def Play():
    User_input = input("Enter a Choice among Rock,Paper, scissors to Play: ").lower()
    Computer_choice = random.choice(("Rock", "Scissors", "Paper")).lower()
    print(Computer_choice)
    if User_input == Computer_choice:
        print(f"Its a tie user choice is {User_input} and Computer input is {Computer_choice}")
    elif User_input == "paper":
        if Computer_choice == "rock":
            print("User Win, Paper covers Rock")
        elif Computer_choice == "Scissors":
            print("Computer wins, Scissors cuts paper")
    elif User_input == "rock":
        if Computer_choice == "paper":
            print("User losses, Paper covers Rock")
        elif Computer_choice == "scissors":
            print("User wins, Rock crushes scissors")
    elif User_input == "scissors":
        if Computer_choice == "paper":
            print("User wins, Scissors cuts paper")
        elif Computer_choice == "rock":
            print("User losses, Rock crushes scissors")
    else:
        print("Check on your input!!")


Play()
