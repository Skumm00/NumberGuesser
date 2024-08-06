import pandas 

import math 

# Initialize variables

score = 0
chances = 5
#starting print statement

print("Oy! Come on down and welcome to the QUIZ game! You will have 5 chances to enter and you and a friend can play with it!")

# Get the guess from the first player

guess = input("Enter a number: ")
if guess == "":
    print("Please enter a guess!")
else:
    guess = int(guess)
    print("Great! Let's begin! Player 1, step back from the computer and let player 2 guess!")

    # Keep doing untill player 2 runs out of chances
  
    while chances > 0:
        guesses = input(f"Now enter a guess! You have {chances} chances left: ")
        guesses = int(guesses)

        if guesses == guess:
            print("Congrats! You guessed it! I'm not sure how, but GREAT job.")
            score += 1
            break
        elif guesses > guess:
            print("Too high! Try again.")
            chances -= 1
        elif guesses < guess:
            print("Too low! Try again.")
            chances -= 1

    if chances == 0:
        print("Sorry mate your OUT. GL next time.")