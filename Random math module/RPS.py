import random

while True:
    user_action = input("Rock, paper, scissors shoot! (type lowercase) ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\n You chose {user_action}, computer chose {computer_action}.")

    if user_action == computer_action:
        print("We tied.")
    elif user_action == "rock":
        if user_action == "rock":
            print("You win cause rock beats scissors.")
        else:
            print("Nuh uh i win.")

    elif user_action == "paper":
        if computer_action == "rock":
            print("you win cause paper eats rock")
        else:
            print("Nuh uh. i win this time buddy")

    elif user_action == "Scissors":
        if computer_action == "paper":
            print("Stop winning please :( i really wanna win")
        else:
            print("yayyyyyyyyyyyyyyyyyyyyyyyyyyy i win :D")
    play_again = input("Play again (yes/no) you must type lowercase ")
    if play_again != "yes":
        print("Okay bye.")
        break