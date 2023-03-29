import time

def print_slowly(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

def start_game():
    print_slowly("Welcome to the Choose Your Own Adventure Game!")
    time.sleep(1)
    print_slowly("You find yourself in a dark forest, with two paths in front of you.")
    time.sleep(1)
    path_choice()

def path_choice():
    print_slowly("Do you want to take the left path or the right path?")
    print_slowly("Type 'left' or 'right' to choose.")
    choice = input().lower()

    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    else:
        print_slowly("Invalid choice, please try again.")
        path_choice()

def left_path():
    print_slowly("You take the left path and encounter a friendly wizard.")
    time.sleep(1)
    print_slowly("The wizard offers you a magical potion.")
    print_slowly("Do you accept the potion? Type 'yes' or 'no'.")
    choice = input().lower()

    if choice == "yes":
        print_slowly("You drink the potion and gain magical powers!")
        print_slowly("Congratulations, you won the game!")
    elif choice == "no":
        print_slowly("You politely decline the wizard's offer and continue on your journey.")
        print_slowly("You eventually get lost and never find your way out of the forest.")
        print_slowly("Game Over.")
    else:
        print_slowly("Invalid choice, please try again.")
        left_path()

def right_path():
    print_slowly("You take the right path and encounter a fearsome dragon.")
    time.sleep(1)
    print_slowly("Do you want to fight the dragon or run away?")
    print_slowly("Type 'fight' or 'run' to choose.")
    choice = input().lower()

    if choice == "fight":
        print_slowly("You bravely charge the dragon, but it's too powerful.")
        print_slowly("The dragon defeats you, and you perish in the battle.")
        print_slowly("Game Over.")
    elif choice == "run":
        print_slowly("You turn around and run away as fast as you can.")
        print_slowly("You eventually find your way back to the starting point.")
        path_choice()
    else:
        print_slowly("Invalid choice, please try again.")
        right_path()

if __
