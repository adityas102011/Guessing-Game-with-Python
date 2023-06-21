# Guessing-Game-with-Python
mport random

def guess_number():
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        attempts += 1
        guess = int(input("Guess a number between 1 and 100: "))

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

def play_again():
    choice = input("Do you want to play again? (y/n): ")
    return choice.lower() == "y"

def main():
    print("Welcome to Guess the Number Game!")

    while True:
        guess_number()
        if not play_again():
            break

    print("Thank you for playing. Goodbye!")

if __name__ == "__main__":
    main()
