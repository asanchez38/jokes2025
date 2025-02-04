#Names: Diego Padilla, Abel Sanchez
# This defines a parameter
def funny_joke(joke_options):
    joke = input("Do you want to hear a joke? (yes,no) ").lower()   #Purpose: Tells the user if they want to hear a funny joke                     
    while joke =="yes":                         #if the person wants to hear a joke  it will keep going
        print('great, lets play')
        question = input(f"Your joke options are {joke_options} ") #displays the lsit of jokes and tells the player to choose one
        if question == 'robbers':                  #if they choose robbers it displays this
            input("Knock Knock ")
            input("Calder ")
            print("Calder police - I've been robbed!")
            joke = input("Do you want to hear another joke or are you finished? ")   #askes if the user wants to hear another joke and keeps it going
        elif question == "tanks":          #this tells them the tanks joke
            input("Knock Knock ")
            input("Tank ")
            print("You are welcome! ")
            joke = input("Do you want to hear another joke or are you finished? ")#askes if the user want to hear another joke
        elif question == "pencils":             #this tells them the pencil joke
            input("Knock Knock ")
            input("Broken pen   cil ")
            print("Nevermind, it's pointless! ")
            joke = input("Do you want to hear another joke or are you finished? ")#askes if the user want to hear another joke
    if joke == 'finished':                                       #if your done with hearing joke finishes and askes 
        rate = int(input("Please rate our game 1-10! "))         #a few questions to see your experience
        final_score = int(rate * 10)                             # asks for the rating and multplies by ten to get a grade
        print(str(final_score) + " percent satisfaction rate")             #this shows what the percentage that they like the game
        friend = input("Would you recommend this game to a friend? ")   # this askes if they would recommend the game to a friend

        if friend == "yes" or friend == "maybe":                #if they say yes or maybe to remmending they game 
            print("Thanks, we appreciate it. ")                 # it displays we appreciate it
        else:
            print("Sorry that you didn't enjoy it. ")           #if they did like their experience we apologies
joke_options = ["tanks", "robbers", "pencils"] #These call the function and creates the list of options
funny_joke(joke_options)   