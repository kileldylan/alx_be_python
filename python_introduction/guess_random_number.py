import random

# Game to guess random number between 1 to 10
def guess_random_number():
    print("Welcome to the Random Number Guessing Game!")
    print("I am thinking of a number between 1 and 10.")
    
    while True:
        secret_number = random.randint(1, 10)  # Generate a new random number
        attempts = 0  # Reset attempts counter

        while True:
            try:
                guess = int(input("Enter your guess: "))
                attempts += 1  # Increment the guess counter

                match guess:
                    case _ if guess == secret_number:
                        print(f"🎉 Congratulations! You guessed the number {secret_number} after {attempts} attempts!")
                        break
                    
                    case _ if guess > secret_number:
                        print("🚀 Oops, your guess is too high. Try again!")
                    
                    case _ if guess < secret_number:
                        print("❄️ Nope, your guess is too low. Give it another shot!")
            except ValueError:
                print("❌ Invalid input! Please enter a number between 1 and 10.")
        
        # Prompt to play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye.")
            break

# Run the game
guess_random_number()
