import streamlit as st
import random

def math_quiz():
    st.title("➗ Math Quiz Game (2 Players)")

    a = random.randint(1, 20)
    b = random.randint(1, 20)
    correct = a + b

    st.write(f"Question for Player 1: What is {a} + {b}?")
    ans = st.number_input("Answer", key="math_answer", step=1)

    if st.button("Submit"):
        if ans == correct:
            st.success("Correct!")
        else:
            st.error("Incorrect!")
