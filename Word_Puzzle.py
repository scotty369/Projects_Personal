'Word Game'

# This is my awesome Word puzzle! I had to compile several functions to prompt a user to guess a word until it has been correctly stated. The program will display the number of guesses it took to get the word correct. 

def initialize_game():
    print("Welcome to the word guessing game!")

def get_guess():
    guess = input("What is your guess?").lower()
    return guess

def update_display(secret, display, guess):
    if len(guess) != len(secret):
        print("Sorry, the guess must have the same number of letters as the secret word.")
        return False
    else: 
        hint = ""
        for i in range(len(secret)):
            if guess[i] == secret[i]:
                hint += secret[i].upper()
            elif guess[i] in secret:
                hint += secret[i]
            else:
                hint += "_"
        if "_" not in hint:
                print("Congratulations! You guessed the word!")
                return True
        return False    

# Make sure to update the play_game funcition as well to rmove the 'display' variable since it's no longer needed.      

def play_game():
    secret = "crazy"
    display = "_" * len(secret)
    guesses = 0

    print("Your hint is:","_" * len(secret))

    while "_" in display:
        guess = get_guess()
        guesses += 1
        if update_display(secret, display, guess):
            print(f"It took you {guesses} guesses.")
            break

initialize_game()
play_game()