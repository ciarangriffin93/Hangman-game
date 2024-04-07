"""
Main file to be used.
"""
# Import libraries
import os
import random
import art_text
import colorama
from colorama import Fore
from words import words
from hangman_stages import live_stages_dict
import string
colorama.init(autoreset=True)


def clear():
    """
    Clear function to clean-up the terminal so things don't get messy.
    """
    os.system("cls" if os.name == "nt" else "clear")


def output_area():
    """
    Print the rules of the game.
    """
    print(art_text.welcome)
    print(
        Fore.YELLOW + "=================== RULE!! ======================")
    print("1. Guess the word and save the man!!")
    print("2. Everytime you can say only a letter.")
    print("3. Number or two than one letter is not valid letter.")
    print(
        "4. If you make incorrect guesses, you will lose,"
        "\n           The man will die!!!")
    print("5. Please enter letters a valid your name")
    print(
        Fore.YELLOW + "=================================================")

    """
    This function validates the username
    enter by the use.
    """
    while True:
        get_name = input('Enter your name: ')[:20]
        clear()

        if get_name.isalpha():
            print(f"{Fore.YELLOW}HELLO!! {get_name}")
            print("\nLet's play Hangman!!\n      Enjoy!!")
            break
        else:
            print(
                f'{get_name}{Fore.RED} is invalid. Please enter a valid name')


def get_valid_word(words):
    """
    The function that retrieves a random word from
    words.py.
    """
    word = random.choice(words)
    while '_' in word or ' ' in word:
        word = random.choice(words)
    return word.lower()


def hangman():
    """
    The function that play a game of hangman
    """

    word = get_valid_word(words)
    word_letters = set(word)
    aplphabet = set(string.ascii_lowercase)
    used_letters = set()

    live = 8

    while len(word_letters) > 0 and live > 0:
        print(
            '\nYou have', live, 'lives stages left, '
            '\nYou have used these '
            '27 European countries.', ' '.join(used_letters))
        # Main game loop
        word_list = [
            letter if letter in used_letters else '_' for letter in word]
        print(Fore.YELLOW + live_stages_dict[live])
        print('current Word:', ' '.join(word_list))
        user_letter = input("Guess a letter: ").lower()
        if user_letter in aplphabet - used_letters:
            used_letters.add(user_letter)
            clear()

            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print(' ')

            else:
                live = live-1
                # Letter incorrectly
                print('\n Your letter', user_letter, 'is not the word')

        elif user_letter in used_letters:
            clear()
            print('\n You have already used the letter. Guess another letter.')

        else:
            clear()
            # Two letters or number is not a valid
            print(Fore.RED + '\n That is not a valid letter')

    if live == 0:
        # The player of defeat
        print(live_stages_dict[live])
        print(Fore.RED + 'You died, sorry! The word was', word)
        print(art_text.died)
    else:
        # The player of victory
        print(Fore.GREEN + 'Well done! You guessed the word was', word)
        print(art_text.win)


def play_game():
    """
    Create a function that provides the option to play the game again.
    Ask the user if they want to play the game again.
    """
    while True:
        restart = input("\nWould you like to play again? (Y/N): ").upper()
        clear()
        if restart == "Y":
            main()
            return True

        if restart == "N":
            print("         Thank you for play! Hope you enjoyed it!!")
            print(art_text.bye)
            return False

        else:
            print("Invalid choice. Please enter 'Y' or 'N'\n")


def main():
    """
    Run functions at the start of the program.
    """
    output_area()
    hangman()
    play_game()


main()
