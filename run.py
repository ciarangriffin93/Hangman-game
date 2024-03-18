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

    word =get_valid_words(words_list)
    word_letter =set(words)
    aplphabet =set(string.ascii_uppercase)
    used_letter =set()

    hangnan-stages = 6

    while len(word_letter) > 0 and hangman_stages > 0:
