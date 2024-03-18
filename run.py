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

def play(word):
    word_complettion = "_" * len(word)
    guessed = false 
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("let's play Hangman!")
    print(display_hangman(tries))
    print(word_complettion)
    print("\n")
    
