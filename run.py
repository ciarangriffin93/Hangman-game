import os
import random 
from words import words
from hangman_stages import live_stages_dict
import string

def clear():
    """
    Clear function to clean-up the terminal so things don't get messy.
    """
    os.system("cls" if os.name == "nt" else "clear")

def output_area():
    """
    Remember to read the rules.
    """
    print(
        "\033[1;33;40m===============\033[1;34;40m WELCOME TO HANGMAN GAME!!"
        "\033[0m\033[1;33;40m===============\033[0m"
)
    print("1. Goal: guess the word and save the man!")
    print("2. Everytime you can say only a letter.")
    print("3. If you make incorrect guesses, you will lose. The man will die!!!")
    print(
        "\033[1;33;40m====================="
        "===================================\033[0m"
)

    """
    The following text: output user sees messages.
    """
    while True:
        get_name = input('Enter your name:')
        clear()

        if get_name.isalpha():
            print(f' HELLO!! {get_name}')
            break
        else:
            print(f'{get_name} is invalid. Please enter a valid name')

def get_valid_word(words):
    """
    Function that retrieves a random word from a list of words stored in a data file. 
    """
    word = random.choice(words)
    while '_' in word or ' ' in word:
        word =random.choice(words)
    
    return word.upper()

def hangman():
    """
    Function that plays the game
    """

    word = get_valid_word(words)
    word_letters = set(word)
    aplphabet = set(string.ascii_uppercase)
    used_letters = set()

    live = 7

    while len(word_letters) > 0 and live > 0:

        print('You have',live, 'live stages left and you have used these letters.')
        print('Let start playing!! ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '_' for letter in word]
        print(live_stages_dict[live])
        print('current Word:' ,' '.join(word_list))
        user_letter = input("Guess a letter: ").upper()
        if user_letter in aplphabet - used_letters:
            used_letters.add(user_letter)

            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print(' ')

            else:
                live = live -1 
                print('\n Your letter', user_letter, 'is not the word')

        elif user_letter in used_letters:
            print('\n You have already used the letter. Guess another letter.') 

        else:
            print('\n That is not a valid letter')


    if live == 0: 
        print(live_stages_dict[live])
        print('You died, sorry! The word was', word)

    else: # end game as user guessed letters
        print('Well done! You guessed the word', word)

def play_game():
    """
    Create a function that provides the option to play the game again." 
    """
    start_over = input("Would you like to play again? enter y for yes or "
                       "If you don't want to play, You can use exit for exit ")                  

    if start_over.lower() == "y":
        main()

    else:
        exit()            

def main():
    clear()
    output_area()
    hangman()
    play_game()

main()    


                       

