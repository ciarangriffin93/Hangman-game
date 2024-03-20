import random 
from words import words
from hangman_stages import live_stages_dict
import string 


def get_valid_word(words):
    """
    Function that retrieves a random word from a list of words stored in a data file. 
    """
    word = random.choice(words)
    while '-' in word or ' ' in word:
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

        print('You have ', live, 'live satges left and you have used these letters: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in words]
        print(live_stages_dict[live])
        print('current Word:' ,' '.join(word_list))
        user_letter = input("Guess a letter: ").upper()
        if user_letter in aplphabet - used_letters:
            used_letters.add(user_letter)

            if user_letter in word_letters:
                used_letters.remove(user_letter)
                print(' ')

            else:
                live = live -1 
                print('\n Your letter', user_letter, 'is not the word')

        elif used_letter in used_letters:
            print('\n You have already used the letter. Guess another letter.') 

        else:
            print('\n That is not a valid letter') 

    if live == 0: 
        print(live_stages_dict[live])
        print('You died, sorry! The word was', word)

    else: # end game as user guessed letters
        print('Well Done!! you guessed the word', word)

if __name__ == '__main__':
    hangman() 


                       

