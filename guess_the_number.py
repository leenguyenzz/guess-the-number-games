import random

def main():
    print("Welcome to Guess the Number!")
    secret_number = random.randint(1, 100)
    guesses_taken = 0

    while True:
        guess = input("Take a guess (1-100): ")
        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid number.")
            continue

        guesses_taken += 1

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job! You guessed it in {guesses_taken} tries.")
            break

if __name__ == "__main__":
    main()
