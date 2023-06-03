#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo

print(logo)
print("I'm thinking of a number between 1 and 100, can you guess it?")

def choose_random_number():
    number = random.randint(1,100)
    return number


def choose_skill_level():
    skill_level = input("Would you like to play 'easy' or 'hard'? ")
    skill_level = skill_level.lower()
    if skill_level == "easy":
        total_guesses = 10
        return total_guesses

    elif skill_level == "hard":
        total_guesses = 5
        return total_guesses
    else:
        print("I'm sorry, I don't recognize that choice. Please start over")
        


def game(number,total_guesses):
    print(f"You have {total_guesses} guesses, choose wisely")
    while total_guesses != 0:
        print(f"You have {total_guesses} guesses left ")
        guess = int(input("What is your guess? "))
        # if total_guesses == 0:
        #     print(f"I'm sorry, you ran out of guesses. The number was {number}.")
        if guess == number:
            print(f"That's correct! The number was {number}. Thank you for playing")
            break
        elif guess > number:
            print("That's too high")
            total_guesses -= 1
            if total_guesses == 0:
                print(f"I'm sorry, you ran out of guesses. The number was {number}.")

        elif guess < number:
            print("That's too low")
            total_guesses -= 1
            if total_guesses == 0:
                print(f"I'm sorry, you ran out of guesses. The number was {number}.")




# def hard():

def run_game():
    
    number = choose_random_number()
    total_guesses = choose_skill_level()
    game(number,total_guesses)

run_game()
