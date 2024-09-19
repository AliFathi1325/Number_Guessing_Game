<!-- @format -->

# Number Guessing Game with Streamlit

This is a simple number guessing game built with Python using the Streamlit framework. The goal is to guess a randomly generated number between 1 and 100 within 5 attempts.

## How the Game Works

- At the start of the game, a random number between 1 and 100 is selected.
- You have 5 chances to guess the correct number.
- After each guess, the game will tell you whether the correct number is higher or lower than your guess.
- If you guess the correct number, you win!
- If you don't guess the correct number within 5 attempts, you lose, and the game will ask you to refresh the page to try again.

## Features

- Random number generation for every new game.
- User input for guesses.
- Feedback after each guess (whether the number is higher or lower).
- Displays remaining attempts.
- Success and failure messages.
- Streamlit’s `session_state` is used to maintain game progress across user interactions.

## How to Run the Game

1. Clone the repository or download the code files.
2. Ensure you have Python and Streamlit installed:
   pip install streamlit
3. Run the Streamlit app:
   streamlit run app.py
4. A web interface will open in your browser, and you can start playing the game.

## How to Play

- Enter your guess in the input box (must be between 1 and 100).
- Click the 'Submit Guess' button.
- The game will inform you if the correct number is higher or lower than your guess.
- Keep guessing until you find the correct number or run out of attempts (5 attempts total).


## Requirements

Python 3.x
Streamlit

## Example

Once the app is running, you will see a simple interface asking you to enter a guess:

You'll receive feedback after each guess, and the game will let you know if you've won or lost!

Enjoy playing the Number Guessing Game!
