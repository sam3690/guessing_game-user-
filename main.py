import random

def guessing_game():
    
    secret_number = random.randint(0, 10)
    
    guess_count = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 0 and 10.")
    
    while True:
        
        try:
            user_guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        guess_count += 1
        
        if user_guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} correctly!")
            print(f"It took you {guess_count} {'guess' if guess_count == 1 else 'guesses'}.")
            break
        elif user_guess < secret_number:
            print("Too low. Try again!")
        else:
            print("Too high. Try again!")

if __name__ == "__main__":
    guessing_game()