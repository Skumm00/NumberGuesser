
# Initialize variables

score = 0
chances = 5

# Starting print statement
print("Oy! Come on down and welcome to the QUIZ game! You will have 5 chances but you can call for a helpline!")

#get the users name 
name = input("What's your name?")
# Get the guess from the first player
guess = int(input("Enter a number from 1-100: "))
if guess > 100:
    print("Please put a number below a hundred!")
    guess = int(input("Enter a number from 1-100: "))
elif guess <= 0:
    print("Please put a number above zero!")
    guess = int(input("Enter a number from 1-100: "))
#inputting the different names
name2 = input("Player 2, whats your name?")
print(f"Great! Let's begin! {name}, step back from the computer and let {name2} guess!")
def keepscore():
    global score 
    global score2
    if score > 5:
        print(f"Congratulations {name}, you won!")
    else:
        print(f"Congratulations {name2}, you won!")

# Now creating the helpline feature
helpline_used = False
def helpline():
    global helpline_used  # Access helpline

    if helpline_used:
        print("Sorry, you've already used the helpline once. No more cheater!")
    elif guess % 2 == 0:
        print("The Number is even!") #getting more things you can get in helpline
        helpline_used = True
    elif guess / 4 == 0:
        print("The Number is divisible by 4!")
        helpline_used = True
    else:
        math = guess * 2
        print(f"Oy! Need some help, eh? Well, you're in luck! The number multiplied by 2 equals {math}! Now you'll get it for sure!")
        helpline_used = True  # Mark helpline as used so cant be modified

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
    print(f"Sorry {name2}, you're OUT. Good luck next time!")
    score += 1

