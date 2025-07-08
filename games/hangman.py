import streamlit as st

def hangman():
    st.title("💀 Hangman Game")

    word = st.text_input("Player 1: Enter a word (hide from Player 2)", type="password")
    guess = st.text_input("Player 2: Guess the word")

    if st.button("Check"):
        if guess.lower() == word.lower():
            st.success("🎉 Correct! You guessed the word!")
        else:
            st.error("Wrong guess. Try again!")
