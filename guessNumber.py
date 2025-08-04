from random import *


def game():
    guessNumber = randint(1, 50)  # Generate once
    attempt = 0

    while True:
        try:
            guessHuman = int(input('Guess the random number: '))

            if guessNumber == guessHuman:
                print("You have guessed the number!")
                break
            elif guessNumber < guessHuman:
                print(f"Too big ! attempt = {attempt}")
                attempt += 1
            else:
                print(f"Too small ! attempt = {attempt}")
                attempt += 1

        except ValueError:
            print("Error: Please enter a valid number.")


game()
