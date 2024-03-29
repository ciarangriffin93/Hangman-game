import os
import random
import art_text
import colorama
from colorama import Fore, Back, Style
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
    Remember to read the rules.
    """
    print(art_text.welcome)
    print(
        Fore.YELLOW + "===============HANGMAN GAME RULE!!===============")
    print("1. Goal: guess the word and save the man!")
    print("2. Everytime you can say only a letter.")
    print(
        "3. If you make incorrect guesses, you will lose,"
        "\n           The man will die!!!")
    print(
        Fore.YELLOW + "=================================================")

    """
    The following text: output user sees messages.
    """
    while True:
        get_name = input('Enter your name:')
        clear()

        if get_name.isalpha():
            print(f"{Fore.YELLOW} HELLO!! {get_name}")
            break
        else:
            print(f'{get_name} is invalid. Please enter a valid name')


def get_valid_word(words):
    """
    Function that retrieves a random word from a list of
    words stored in a data file.
    """
    word = random.choice(words)
    while '_' in word or ' ' in word:
        word = random.choice(words)
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
        print(
            'You have', live, 'lives stages left and '
            'you have used these letters: ', ' '.join(used_letters))
        print(
            'Let start playing!!'
            '\n     Enjoy!!')

        word_list = [
            letter if letter in used_letters else '_' for letter in word]
        print(Fore.YELLOW + live_stages_dict[live])
        print('current Word:', ' '.join(word_list))
        user_letter = input("Guess a letter: ").upper()
        if user_letter in aplphabet - used_letters:
            used_letters.add(user_letter)
            clear()

            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print(' ')

            else:
                live = live-1
                print('\n Your letter', user_letter, 'is not the word')

        elif user_letter in used_letters:
            print('\n You have already used the letter. Guess another letter.')

        else:
            print('\n That is not a valid letter')

    if live == 0:
        print(live_stages_dict[live])
        print(Fore.RED + 'You died, sorry! The word was', word)
    else:
        print(Fore.GREEN + 'Well done! You guessed the word', word)


def play_game():
    """
    Create a function that provides the option to play the game again.
    """
    start_over = input(
        "Would you like to play again? enter y for yes or "
        "\nIf you don't want to play, "
        "enter n for no ")
    clear()

    if start_over.lower() == "y":
        main()

    else:
        print("Thank you for play!\nHope you enjoyed it!!")
        print(art_text.bye)
        exit()


def main():
    output_area()
    hangman()
    play_game()


main()