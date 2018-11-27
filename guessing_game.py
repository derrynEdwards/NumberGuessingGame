"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random

def get_prompt():
    while True:
        prompt = input("Please enter a number from 1-20: ")
        try:
            guess = int(prompt)
            if guess < 1 or guess > 20:
                raise ValueError("Number not in range!")
        except ValueError:
            print("Wrong input. Try again!")
        else:
            return guess


def guess_number(number):
    tries = 0
    number = number

    while True:
        guess = get_prompt()

        if guess < number:
            print("The correct number is higher!")
            tries += 1
        elif guess > number:
            print("The correct number is lower!")
            tries += 1
        elif guess == number:
            tries += 1
            print("Correct!")
            return tries


def generate_number():
    number = int(20 * random.random())
    if number == 0:
        number += 1

    return number


def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    print("""
====================================
Welcome to the Number Guessing Game!
      Good Luck and Have Fun!
====================================
""")
    #set a random number from 1 - 20 inclusive.
    high_score = 0
    current_score = 0
    number = generate_number()
    
    while True:
        tries = guess_number(number)
        current_score = tries
        print("Number of attempts: {}".format(tries))

        if high_score == 0:
            high_score = current_score
        elif current_score < high_score:
            high_score = current_score
  
        while True: 
            play_again = input("Would you like to play again? Yes (y) / No  (n)? ")

            if play_again == 'y':
                print("Generating new number...")
                number = generate_number()
                print("Your Current High Score is: {}".format(high_score))
                break
            elif play_again == 'n':
                print("Thanks for playing! Goodbye!")
                break           
            else:
                print("Wrong input. Try again!")
                continue

        if play_again == 'n':
            break
                
        


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
