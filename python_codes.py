import random

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == "stone" and computer_choice == "scissors") or
        (player_choice == "paper" and computer_choice == "stone") or
        (player_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    choices = ["stone", "paper", "scissors"]

    while True:
        player_choice = input("Enter your choice (stone, paper, or scissors): ").lower()
        if player_choice not in choices:
            print("Invalid input. Please try again.")
            continue

        computer_choice = random.choice(choices)

        print(f"\nYou chose: {player_choice}")
        print(f"Computer chose: {computer_choice}\n")

        winner = determine_winner(player_choice, computer_choice)
        print(winner)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    print("Thanks for playing!")

play_game()
