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

    hangnan_stages = 7

    while len(word_letter) > 0 and hangman_stages > 0:

        print('You have ', hangman_stages, 'hangman satges left and you have used these letter: ', ' '.join(used_letter))

        words_list = [letter if letter in used_letter else '-' for letter in words]
        print(hangman_stages_num)
        print('current Word:' ,' '.join(words_list))

        user_letter = input("Guess a letter: ").upper()
        if used_letter in aplphabet -used_letters:
            used_letter.add (user_letter)

            if user_letter in word_letter:
                words used_letters.remove(user_letter)
                print(' ')

            else:
                hangman_stages =hangman_stages -1 
                print('\n Your letter', user_letter, 'is not the word')

        elif used_letter in used_letters:
            print('\nYou have already used the letter. Guess another letter.') 

        else:
            print('\n That is not a valid letter') 

    if hangman_stages ==0: # end once the user reaches the maximum number of errors allowed
        print(hangman_stages_num[hangman_stages])
        print('You died, sorry! The word was', words)

    else: # end game as user guessed letters
        print('YAY! you guessed the word', words)

if __name == __main__ 

    hangman() 


                       

