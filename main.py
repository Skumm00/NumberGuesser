import pandas 

import math 
# Initialize variables

score = 0
chances = 5

# Starting print statement
print("Oy! Come on down and welcome to the QUIZ game! You will have 5 chances but you can call for a helpline!")

# Get the guess from the first player
guess = int(input("Enter a number from 1-100: "))
if guess > 100:
    print("Please put a number below a hundred!")
    guess = int(input("Enter a number from 1-100: "))
elif guess <= 0:
    print("Please put a number above zero!")
    guess = int(input("Enter a number from 1-100: "))
else:
    print("Please put a proper number")
    guess = int(input("Enter a number from 1-100: "))  # Runs all the checks

print("Great! Let's begin! Player 1, step back from the computer and let player 2 guess!")

# Keep doing until player 2 runs out of chances
while chances > 0:
    guesses = input(f"Enter a number or select 0 for a helpline. You have {chances} chances left: ")
    guesses = int(guesses)

    if guesses == guess:
        print("Congrats! You guessed it! I'm not sure how, but GREAT job.")
        score += 1
        break
    elif guesses == 0:
      print("Getting a clue!")
      helpline()
  
    elif guesses > guess:
        print("Too high! Try again.")
        chances -= 1
      
    elif guesses < guess:
        print("Too low! Try again.")
        chances -= 1

if chances == 0:
    print("Sorry mate, you're OUT. Good luck next time!")

# Now creating the helpline feature
helpline_used = False

def helpline():
    global helpline_used  # Acces helpline

    if helpline_used:
        print("Sorry, you've already used the helpline once. No more cheater!")
    else:
        math = guess * 2
        print(f"Oy! Need some help, eh? Well, you're in luck! The number multiplied by 2 equals {math}! Now you'll get it for sure!")
        helpline_used = True  # Mark helpline as used so cant be modified