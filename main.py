# Initialize variables
score = 0
score2 = 0
chances = 5

# Starting print statement
print("Oy! Come on down and welcome to the QUIZ game! You will have 5 chances but you can call for a helpline!")

game_mode = int(input("Choose a game mode:\n1. Play with someone else\n2. Use random number generator\nEnter 1 or 2: "))

if game_mode == 1:
    #get the name of player 1
    name = input("What's your name? ")
  #get the name of player2
    name2 = input("Player 2, what's your name? ")

    guess = int(input(f"{name}, Enter a number from 1-100: "))
    while guess <= 0 or guess > 100:
        print("Please enter a number between 1 and 100!")
        guess = int(input("Enter a number from 1-100: "))

    print(f"Great! Let's begin! {name}, step back from the computer and let {name2} guess!")
    win = False
    def keepscore():
        global score 
        global score2
        if not win:
          score = score + 1
          if score > 5:
            print(f"Congratulations {name}, you won!")
        else:
          score2 = score + 1
          if score > 5:
            print(f"Congratulations {name}, you won!")
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
            helpline_used = True  # Mark helpline as used so cant be modified
    # Keep doing until player 2 runs out of chances
    while chances > 0: #actual game logic
        guesses = input(f"Enter a number or select 0 for a helpline. You have {chances} chances left: ")
        guesses = int(guesses)
        if guesses == guess:
            print("Congrats! You guessed it! I'm not sure how, but GREAT job.")
            keepscore()
            win = True
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
        keepscore()
        win = True
    win = False
elif game_mode == 2:
  print("Game Mode 2: Random Number Generator")
  #logic: seed for the inital value, n for the digits in the seed(4 default), iterations for how many times you want it, mininum number is 1, and max number is 100.
  def genrandom(seed,n = 4, iterations = 5, min = 1, max = 100):
    
    #empty array for the list of numbers
    result = []
    #go through iterations(only 5 times we need)
    for _ in range(iterations):
      
      #this is simple math to square the seed 
      seed_squared = seed ** 2 
      #makes sures no empty space by putting 0's
      seed_string = str(seed_squared).zfill(2 * n) 
      #uses slicing so  we get middle digit using integer division 
      middle_digit = seed_string[n // 2 : n + n // 2]
      next_seed = int(middle_digit) #turn middle digit BACK into an integer
      
      #Now we scale the number using min and max
      scalednumber = min + (next_seed % (max - min + 1))
      #scales by dividing the seeed(next_seed) and dividing it by the range size(max-min +1) and then adding to the min value 
      
      result.append(scalednumber) #append/ add the scaled number to the result list
      seed = next_seed # repeats the process until the iterations are all through
      
  example_seed = 68
  random_num = genrandom(example_seed)
  
  guess = random_num
  #now guess equals to the random number and all we have to do is put the if and else statements
else:
    print("Invalid choice. Please select 1 or 2. 1 for playing with someone else, 2 for random number generator.")
