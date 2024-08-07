import random
# Initialize variables
score = 0
score2 = 0
chances = 5

# Define the keepscore function outside both if statements
def keepscore():
    global score 
    global score2
    global play
    if not win:
        score = score + 1
        if score > 5:
            print(f"Congratulations {name}, you won!")
    else:
        score2 = score + 1
        if score > 5:
            print(f"Congratulations {name}, you won!")
    print(f"{name} has {score} points! {name2} has {score2} points!")
        if play = True and score > 5: 
            print(f"Congrats! {name2}, you won!")
        else: 
            score2 = score2 + 1 
        print(f"{name} has {score} points! {name2} has {score2} points!")
# Now creating the helpline feature
helpline_used= False
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
        helpline_used = True # Mark helpline as used so cant be modified

#Now defining the call quesion function
win = False

#Gives the questions
selecter_choice = f"Great! Let's begin! {name}, step back from the computer and let {name2} guess!"
def questions():
    chances =  5
    print(selecter_choice)
    win = False
    # Keep doing until player 2 runs out of chances
    while chances > 0: #actual game logic
        win = False
        guesses = input(f"Enter a number or select 0 for a helpline. You have {chances} chances left: ")
        guesses = int(guesses)
        if guesses == guess:
            print("Congrats! You guessed it! I'm not sure how, but GREAT job.")
            keepscore()
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
        print(f"Sorry, you're OUT. Good luck next time!")
        keepscore()
        win = True
    win = False

#if user wants to play again
play = False
def playagain():
    user_choice = input("Want to Play Again? yes/no")
    if user_choice.lower() == "yes":
        play = True 
    elif user.choice.lower() == "no":
        play = False 
    if play = True and game_mode == 1:
        selector_choice = f"Great! Lets's begin! {name2}, step back from the computer and let {name} guess!"
        print(selector_choice)
# Starting print statement
print("Oy! Come on down and welcome to the QUIZ game! You will have 5 chances but you can call for a helpline!") 
game_mode = int(input("Choose a game mode:\n1. Play with someone else\n2. Use random number generator\nEnter 1 or 2: "))
#the different choices
if game_mode == 1:
    #get the name of player 1
    name = input("What's your name? ")
  #get the name of player2
    name2 = input("Player 2, what's your name? ")

    guess = int(input(f"{name}, Enter a number from 1-100: "))
    while guess <= 0 or guess > 100:
        print("Please enter a number between 1 and 100!")
        guess = int(input("Enter a number from 1-100: "))
    questions()
elif game_mode == 2:
  print("Game Mode 2: Random Number Generator")
  #logic: seed for the inital value, n for the digits in the seed(4 default), iterations for how many times you want it, mininum number is 1, and max number is 100.
  #gives the function generate_random
  def generate_random(iterations=1, min_value=1, max_value=100):
      # a list with the result
      result = []
      #a for  in range loop that will iterate how many times you want thrugh the iteration
      for _ in range(iterations):
          #gives of a random number from the randomint
          random_number = random.randint(min_value, max_value)
        #appends this random_number to the result list
          result.append(random_number)
        #finnaly returns the result
      return result[0]
  #declares the variables so now the user can guess them!
  random_numbers = generate_random()
  guess = random_numbers
  name2 = input("Before you face the computer, whats your name?")
  name = "PC"
  questions()
