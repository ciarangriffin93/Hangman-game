import random 
from wrods import words_list

def game_rules(data):
    """
    Checks if player want to read the rules.
    """
    if data == "Y":
        print(word_art.rules_style)
        print("=======================================================")
        print("For name words\n")
        print("3. If you guess correct the letter will appear in the word.\n")
        print("4. If you guess all the letters in the word, you win.\n")
        print("5. If you guess incorrect a body part adds to Hangman.")
        print("The more body parts the Hangman have..")
        print("..the closer you are to lose.\n")
        print("=======================================================")
        return True
    elif data == "N":
        return True
    else:
        print(" Please enter 'Y' or 'N'.")


def get_words():
    word = random.choice(words_list)
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
    
