## Hangman Game

The Hangman game is a Python terminal deployed to Heroku.

This game is to guess a random word letter by letter. If the player makes too many incorrect guesses, the man is a hangman. If the player correctly guesses the word, the man survives.

Click [here](https://hangman-game-30a164540c0f.herokuapp.com/) to see the live site.

![Image of Dvice responsivneness](/documentation/images/herokuapp.png)

---

## How to play

This game is based on the hangman game:

* The hangman will select a word related to European countries.

* The hangman draws a line for each letter in the word.

* The guesser will guess one letter at a time. If the letter is in the word, the hangman will fill in the blanks with the correct guesses.

* If the letter is not in the word, the hangman will draw one body part for each incorrect guess: head, body, arm, and leg.
---

## User Stories

* As a user, I want to start a new game so that I can begin playing Hangman from scratch.

* As a user, I want the hangman game to be more user-friendly.

* As a user, I want to visit hangman game to learn more.

* As a user, I want the option to play again after completing or lose a game that I can continue enjoying the Hangman experience. 
---

## Features

* The game show.
  * Welcome to the Hangman game!
  * The player has read the game rules.

![Image of game show](/documentation/images/game-rule.png)

* Name request input.
  * When the player enters their name, they will receive a welcome message.

![Image of name request](/documentation/images/enter-name.png)

* Name invalid
  * Enter a Number and space is not a valid name. 

![Space-Invalid](/documentation/images/space-invalid.png)

![Number-Invalid](/documentation/images/numbers-invalid.png)

* Show the instructions.
  * The game starts by showing live stages and a word, and then it starts the game.

![Image of instructions](/documentation/images/instructions%20.png)

* Guess a letter.
  * Players can press any letter of the alphabet on their keyboard to start the game.

![Image of guess a letter](/documentation/images/guess-letter.png)

* Guess correct. 
  * If the guessed letter is correct, a message is sent confirming its placement in the word.

![Image of correct](/documentation/images/guess-correct.png)

* Guess incorrect.
  * If the guessed letter is incorrect, players will receive a message indicating that the letter is not in the word.

![Image of incorrect](/documentation/images/guess-incorrect.png)

* Letter and number invalid 
  * Two than one letter or number is not vnvalid

![letters-number-invalid](/documentation/images/two-letter-invalid.png)

* Game win.
  * Players win the game by correctly guessing all the letters in the word. Once they do this, they receive a message informing them that they have guessed the word and won the game.

![Image of game win](/documentation/images/win-game.png)

* Game lose.
  * Players lose the game when they exhaust all incorrect guesses and the full graphic is displayed. In this scenario, they receive a message stating that they have lost.

![Image of game lose](/documentation/images/lose-game.png)

* Play again.
   * If the player want to play "start_over == 'y'"
	* If the player chooses not to "play start_over == 'n'"

![Image of game again](/documentation/images/play-again.png)

* End game.
  * If they don't want to play again, a "Thank you for play and hope you enjoyed it. BYE!" message will be displayed.

![Image of game end](/documentation/images/end-game.png)

---

## Future Feature

* Implement different difficulty levels easy, medium, hard" with word lengths to cater to players of different skill levels.

* Players to choose from different themes or categories for the words, such as animals, movies, history, or sports.
---

## Flowchart

I used Canva to plan and map out the core processes.

![Canva](/documentation/flowchart/canva)

---

## Testing

* For all testing, please refer to the following [TESTING.md](/TESTING.md) file
---

## Deployment

Code Institute has provided a [template](https://github.com/Code-Institute-Org/python-essentials-template) to display the terminal view of this backend application in a modern web browser.
This is to improve the accessibility of the project to others.

The live deployed application can be found deployed on [Heroku](https://hangman-game-30a164540c0f.herokuapp.com).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Heroku needs three additional files in order to deploy properly.

- requirements.txt
- Procfile
- runtime.txt

You can install this project's **requirements** (where applicable) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:

- `echo web: node index.js > Procfile`

The **runtime.txt** file needs to know which Python version you're using:
1. type: `python3 --version` in the terminal.
2. in the **runtime.txt** file, add your Python version:
	- `python-3.9.18`

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:


### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.

- `pip3 install -r requirements.txt`.

If using any confidential credentials, such as `CREDS.json` or `env.py` data, these will need to be manually added to your own newly created project as well.

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/ciarangriffin93/Hangman-game) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/ciarangriffin93/Hangman-game.git`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/ciarangriffin93/Hangman-game)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/ciarangriffin93/Hangman-game)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!
---

## Technologies Used

#### languages used:

* [Python](https://www.python.org/): Used to provide functionality to the site.

* [Git](https://git-scm.com): Used write Git to commit and push the code for the development of the website. 

* [Gitpod](https://gitpod.io): Cloud IDE was used to write, commit, and push code to GitHub.

* [Github](https://github.com): Used frequently to commit and push code.

* [Heroku](https://dashboard.heroku.com/apps): Deploy a live version of the terminal.

* [Fancy text pro](https://www.fancytextpro.com/): Used to create art with text.

* [Canva](https://www.canva.com/online-whiteboard/flowcharts/): Used create a flowchart for project preparation.

* [CI Python Linter](https://pep8ci.herokuapp.com/): Used display warnings and errors to assess code quality.

#### Python Packages Used:

* [Colorama](https://pypi.org/project/colorama/): Used to add color for visual feedback.

* [Import os](https://stackoverflow.com/questions/2084508/clear-terminal-in-python): Used to clear function for keeping the terminal clean.

#### Tools:

* Use the correct template from CI:
  * https://github.com/Code-Institute-Org/p3-template

* Optionally install these extensions:
  * flake8 (basic linter - validate your code in the problems tab)

  * autopep8 (basic formatter)

  * pylint (only for more advanced/complex suggestions)

* Validate by copy/pasting here:
  * https://pep8ci.herokuapp.com/#

* Documentation for validation here:
  * https://pep8.readthedocs.io/en/release-1.7.x/intro.html
---

## Credits

#### content:

* [Youtube](https://www.youtube.com/watch?v=m4nEnsavl6w&t=466s): This is used for learning how to create a hangman game in Python.

* [Colorama youtube](https://www.youtube.com/watch?v=u51Zjlnui4Y): This is used to how do import Colorama into Python.

* [W3schools](https://www.w3schools.com/python/): This site was created using information W3Schools.

* [OS](https://docs.python.org/3/library/os.html): This is how to use the OS module to clear the terminal.

* [Code Institute](https://www.youtube.com/watch?v=WTll5p4N7hE): This is from code institute to learn how to create love sandwiches project.

* [Git Commit](https://www.freecodecamp.org/news/how-to-write-better-git-commit-messages/): I learn how to writing better commit messages.
---

## Acknowledgements

* I would like to thank to my mentor, Tim Nelson and Rory Sheridan for his help and unwavering support.

* I would like to thank to my tutor at Code Institute for their help and unwavering support.

* I would like to thank to my family for their patience, support, and understanding.

* I would like to Code Institute's Slack community,and Deaf group for their support.
---