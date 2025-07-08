import streamlit as st

def word_chain():
    st.title("🔗 Word Chain Game")

    word1 = st.text_input("Player 1: Enter a word")
    word2 = st.text_input("Player 2: Enter next word starting with last letter of previous")

    if st.button("Check"):
        if word1 and word2:
            if word2[0].lower() == word1[-1].lower():
                st.success("Valid chain!")
            else:
                st.error("Word does not start with correct letter.")
