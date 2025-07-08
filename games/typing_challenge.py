import streamlit as st
import time

def typing_challenge():
    st.title("⌨️ Typing Speed Challenge (2 Players)")

    sentence = "The quick brown fox jumps over the lazy dog"

    st.write("Type this sentence as fast as you can:")
    st.code(sentence)

    if st.button("Start"):
        start = time.time()
        typed = st.text_input("Type here and press Enter:")
        end = time.time()

        if typed == sentence:
            duration = end - start
            st.success(f"Correct! Time taken: {duration:.2f} seconds")
        else:
            st.error("Typed incorrectly!")
