## Testing

* I tested the run.py file, and there were no errors or warnings.

![Image of no errors](/documentation/testing/no-errors.png)

### Manual testing

* Manually tested the game the following:

| Action        | Expected Behaviour  | Result | 
| ------------- | ------------- | ------------- |
| Player enters name | Will prompt the player to word to guess. | pass |
| Enter a number, space and hit enter  | Display Invalid input: Please enter letters a valid your name. | pass |
| Enter two than one letter and hit enter | Display Invalid input: Please enter a single letter.  | Pass |
| Enter Number and hit enter | Display Invalid input: Please enter using a letter. | Pass |
| Enter a correct letter and hit enter | Will display letter is correct word. | pass |
| Enter an incorrect letter and hit enter| Will display letter is not the word. | Pass |
| Enter a letter that has been previously guessed and hit enter | Will display You have already used the letter. | Pass |
| Guess the word before attempts are finished| Will display Well done! You guessed the word was | Pass |
| Attempts finished | Will display You died, sorry! The word was. | Pass |
| Letter is incorrect | incorrect guesses left  decrement by 1 | pass | 
| Letter is incorrect | A piece of the graphic is show. | pass | 
| Press 'Y' to play again|  The game will replay. | Pass | 
| Press 'N' to finish the game | Will display Thank you for play! Hope you enjoyed it!! Bye! End of game. | Pass |
| Press 'N' with any other key to enter | Will display Invalid choice. Please enter 'Y' or 'N | Pass |

#### Fixed Bugs

* The only unfixed issue is the warning that came up in CI Python linter on my code, and it raised a few issues, which are displayed in the image below.

* Line too long.
  * Fix this error was raised as a result of the line of code being too long.

* Trailing whitespace.
  * Fix the issue was resolved by removing the white space. This is self-explanatory.

* Blank line contains white space.
  * Fix the self-explanatory warning was resolved by removing the white spaces on a blank line.

![Image of test issues](/documentation/testing/test-issues.png)

* The problem with this code to requires the user press 'n' specifically to exit, but also allow them to exit with any other key. So I have changed the code.

![Press](/documentation/testing/input-y.png)

* I have fixed the code to require the user to press 'n' specifically to exit, and any other key doesn't exit the program. This make it clear to the user that 'n' is the specific key they need to press to exit, and other keys won't have the same effect. 

![press](/documentation/testing/input-y:n.png)


#### Unfixed bugs
* No unfixed bugs.