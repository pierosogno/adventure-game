import random

def main():
    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess the number?")

    secret_number = random.randint(1, 100)
    user_attempts = 0

    while True:
        try:
            user_guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input! Please enter an integer.")
            continue

        user_attempts += 1

        if user_guess == secret_number:
            print(f"Congratulations! You guessed the number in {user_attempts} attempts.")
            break
        elif user_guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

        if user_attempts % 5 == 0:
            print(f"You have made {user_attempts} attempts so far.")

if __name__ == "__main__":
    main()
