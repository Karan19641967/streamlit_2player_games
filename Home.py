import streamlit as st
from games import (
    tic_tac_toe,
    rock_paper_scissors,
    number_guessing,
    hangman,
    math_quiz,
    typing_challenge,
    connect4,
    memory_match,
    word_chain,
    flag_guess,
    country_capital
)

st.set_page_config(page_title="🎮 2 Player Game Hub", layout="centered")

st.title("🎮 2 Player Game Hub")
st.markdown("Choose a game to play together!")

games_dict = {
    "Tic Tac Toe": tic_tac_toe.tic_tac_toe,
    "Rock Paper Scissors": rock_paper_scissors.rock_paper_scissors,
    "Number Guessing": number_guessing.number_guessing,
    "Hangman": hangman.hangman,
    "Math Quiz": math_quiz.math_quiz,
    "Typing Challenge": typing_challenge.typing_challenge,
    "Connect 4": connect4.connect4,
    "Memory Match": memory_match.memory_match,
    "Word Chain": word_chain.word_chain,
    "Flag Guess": flag_guess.flag_guess,
    "Country Capital": country_capital.country_capital,
}

game = st.selectbox("🎲 Select Game", list(games_dict.keys()))
games_dict[game]()  # Call selected game
