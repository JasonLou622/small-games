import random

def guess_the_number():
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 5

    print('*' * 40)
    print("Welcome to 'Guess the Number'!")
    print('*' * 40)
    print(f"I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess the number.\n")

    while attempts < max_attempts:
        guess_input = input(f"Attempt {attempts + 1}/{max_attempts}: Enter your guess: ")

        if not guess_input.isdigit():
            print("Invalid input. Please enter a valid number.\n")
            continue
        guess = int(guess_input)
        attempts += 1

        if guess < secret_number:
            print("Too low! Try a higher number.\n")
        elif guess > secret_number:
            print("Too high! Try a lower number.\n")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
    else:
        print(f"Sorry, you've used all your attempts. The number was {secret_number}.")

if __name__ == "__main__":
    guess_the_number()