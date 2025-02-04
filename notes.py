# Code Requirements
# Input: Use any valid input source such as a keyboard, mouse, microphone, data stream, or file.
# Output: Must depend on the input provided.
# List Usage:
# Must justify why a list is better than alternatives.
# Examples include picking items, random selections, or using list methods like append.
# Function Requirements:
# Must have a parameter.
# Include sequencing (multiple lines of code).
# Utilize selection (e.g., if/else statements).
# Use iteration (e.g., loops like for or while).
# Take different paths based on parameter values.
import random
def greet(name):
   print (f"hello",name)
greet("user")


joke = input("Do you want to hear a joke?") #ask user if they want to hear a joke
if joke == "no":
        print("Okay, suit yourself.") #if they said no, they won't hear a joke
elif joke == "yes":
        print("Great, let's play!") #however, if they say yes, they will
else:
        print("Please respond with 'yes' or 'no'.")
        exit() #asks the user to either say yes or no if they didn't put it down correctly

        # tell_joke()
 #asks the user for a num. 1-3 so they could recieve their joke!
try:
        question = int(input("Choose a number (1-3) to find out your joke: "))
except ValueError:
        print("Please enter a valid number between 1 and 3.")
        exit()

def play_joke_game(choice):
      #List of jokes
        if choice == 1:
                print("Congrats! You got robbers!")
                input("Knock Knock ")
                input("Calder")
                print("Calder police - I've been robbed!")
             
        elif choice == 2: # another joke for the user to see if they get the joke about tanks
                print("Congrats! You got tanks!")
                input("Knock Knock ")
                input("Tank ")
                input("You are welcome!")
               
               
        elif choice == 3: # having the user pick out a game that the computer is giving
          print ("Congrats! you got pencil!")
          input("Knock Knock ")
          input("Broken pencil ")
          input("Nevermind, it's pointless! ")
   
        else:
              print("invalid choice. Please restart this game from 1 and 3")
              exit()
play_joke_game(question)
         
def rate_game(): # This is for the rating of the game to show how good it is
    rating = input("Would you like to rate this game from 1-10? (yes/no): ") # Putting this question to ask the user
    if rating == "yes":
            rate = int(input("Please provide your rating (1-10): "))
            if 1 <= rate <= 10:
                print(f"Thank you for your rating of {rate}! We're glad you enjoyed the game.")
            else:
                print("Please enter a valid rating between 1 and 10.")
    else:
        print("Okay, thank you for playing!")

rate_game()

def friend(): # This is to recommend the game
    recommendation = input("Would you recommend this game to your friends? (yes/maybe/no): ")
    if recommendation == "yes":
        print("Thank you! We appreciate your support.")
    elif recommendation == "maybe":
        print("Thanks for your feedback. We'll work on improving the game!")
    elif recommendation == "no":
        print("We're sorry you didn't enjoy the game.")
    else:
        print("Please answer with 'yes', 'maybe', or 'no'.")
friend()
