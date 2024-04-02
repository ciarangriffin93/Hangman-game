## Hangman Game

The Hangman game is a Python terminal game deployed to Heroku. Players attempt to guess a random word. Incorrect guesses result in a man being drawn piece by piece. If the word is guessed before the entire figure is displayed, the players win otherwise they lose.

Click [here](https://hangman-game-30a164540c0f.herokuapp.com/) to see the live website.

![Image of Dvice responsivneness](/documentation/images/screenshot-game.png)

## How to play

This game is based on the hangman game:

* The hangman will select a word related to European countries.

* The hangman draws a line for each letter in the word.

* The guesser will guess one letter at a time. If the letter is in the word, the hangman will fill in the blanks with the correct guesses.

* If the letter is not in the word, the hangman will draw one body part for each incorrect guess: head, body, arm, and leg.

## Flowchart

![Canva](/documentation/images/canva)

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

## Technologies Used

languages used:

* [Python](https://www.python.org/): Used to provide functionality to the site.

* [Git](https://git-scm.com): Used write Git to commit and push the code for the development of the website. 

* [Gitpod](https://gitpod.io): Cloud IDE was used to write, commit, and push code to GitHub.

* [Github](https://github.com): Used frequently to commit and push code.

* [Heroku](https://dashboard.heroku.com/apps): Deploy a live version of the terminal.

* [OS](https://docs.python.org/3/library/os.html): Used to clear the terminal.

* [Fancy-text-pro](https://www.fancytextpro.com/): Used to create art with text.

* [Canva](https://www.canva.com/online-whiteboard/flowcharts/): Used create a flowchart for project preparation.

* [CI-Python-Linter](https://pep8ci.herokuapp.com/): Used display warnings and errors to assess code quality.