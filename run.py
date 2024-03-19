import random 
from words import words_list
from hangman_stages import hangman_stages_num
import string 


def get_valid_words(words_list):
    """
    Function that retrieves a random word from a list of words stored in a data file. 
    """
    word = random.choice(words_list)
    while '-' in words or ' ' in words:
        word =random.choice(words_list)
    
    return word.upper()

def hangman():
    """
    Function that plays the game
    """

    word =get_valid_words(words_list)
    word_letter =set(words)
    aplphabet =set(string.ascii_uppercase)
    used_letter =set()

    hangnan-stages = 6

    while len(word_letter) > 0 and hangman_stages > 0:

        print('You have ', hangman_stages, 'hangman satges left and you have used these letter: ', ' '.join(used_letter))

        words_list = [letter if letter in used_letter else '-' for letter in words]
        print(hangman_stages_num)
        print('current Word:' ,' '.join(words_list))

        user_letter = input("Guess a letter: ").upper()
        if used_letter in aplphabet -used_letters:
            used_letter.add (user_letter)

            if user_letter in word_letter:
                word used_letter.remove(user_letter)
                print(' ')

