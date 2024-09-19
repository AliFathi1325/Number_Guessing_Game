import random
import streamlit as st

if 'answer' not in st.session_state:
    st.session_state.answer = random.randrange(1, 101)
    st.session_state.round = 1
    st.session_state.round_list = [0]
    st.session_state.guess_list = []

if max(st.session_state.round_list) >= 5:
    if st.session_state.answer in st.session_state.guess_list:
        st.info('Refresh the page to restart the game.')
    else:
        st.error('You lost, refresh the page to start the game again.')

if max(st.session_state.round_list) < 5:
    st.title("Number Guessing Game")
    st.write("""
        In this game you have to guess a number between 1 and 100.
        You have 5 chances to find the correct number.
        After each guess, you will be told if your number is greater or less than the integer.
        If you can't find the correct number after 5 guesses, it's game over
    """)

    guess = st.number_input('Enter your guess:', min_value=1, max_value=100, step=1)

    if st.button('Submit Guess'):
        if st.session_state.round == 5:
            st.write('Unfortunately, you lost')
        elif guess == st.session_state.answer:
            st.success(f"Congratulations! The correct number was {st.session_state.answer}. You guessed it in {st.session_state.round} attempts.")
            st.balloons()
            st.session_state.round = 5
            st.session_state.guess_list.append(guess)
            st.session_state.round_list.append(st.session_state.round)
        else:
            st.session_state.round += 1
            st.session_state.guess_list.append(guess)
            st.session_state.round_list.append(st.session_state.round)

            st.write(f'The number you guessed: {st.session_state.guess_list}')

            if guess < st.session_state.answer:
                st.info("The integer is greater than your guess.")
            elif guess > st.session_state.answer:
                st.info("The integer is smaller than you guessed.")

            attempts_left = 6 - st.session_state.round
            st.error(f"Attempts remaining: {attempts_left}")
