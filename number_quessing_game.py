import random

def number_guessing_game():
    print("🎯 Welcome to the Number Guessing Game!")
    lower = 1
    upper = 100
    secret_number = random.randint(lower, upper)
    attempts = 7

    print(f"Guess the number between {lower} and {upper}. You have {attempts} attempts.")

    for i in range(1, attempts + 1):
        try:
            guess = int(input(f"Attempt {i}: Your guess → "))
        except ValueError:
            print("⚠️ Please enter a valid integer.")
            continue

        if guess < lower or guess > upper:
            print(f"⚠️ Your guess must be between {lower} and {upper}.")
        elif guess < secret_number:
            print("🔼 Too low!")
        elif guess > secret_number:
            print("🔽 Too high!")
        else:
            print(f"🎉 Congratulations! You guessed the number in {i} attempts.")
            break
    else:
        print(f"❌ Out of attempts! The number was: {secret_number}")

    # Ask to play again
    play_again = input("🔁 Do you want to play again? (yes/no): ").strip().lower()
    if play_again in ['yes', 'y']:
        number_guessing_game()
    else:
        print("👋 Thanks for playing!")

# Run the game
number_guessing_game()
