import streamlit as st

def number_guessing():
    st.title("🎯 Number Guessing (2 Player)")
    
    if "secret_number" not in st.session_state:
        st.session_state.secret_number = None
        st.session_state.guess = None
        st.session_state.attempts = 0
        st.session_state.feedback = ""
        st.session_state.locked = False

    if not st.session_state.locked:
        st.subheader("👤 Player 1: Set the secret number")
        secret = st.text_input("Enter a number between 1 and 100", type="password")

        if st.button("Lock the number"):
            if secret.isdigit() and 1 <= int(secret) <= 100:
                st.session_state.secret_number = int(secret)
                st.session_state.locked = True
                st.success("Number locked! Player 2 may now start guessing.")
            else:
                st.error("Please enter a valid number between 1 and 100.")
    else:
        st.subheader("🕵️ Player 2: Try to guess the number!")
        guess = st.number_input("Enter your guess", min_value=1, max_value=100, step=1)
        
        if st.button("Guess"):
            st.session_state.attempts += 1
            if guess < st.session_state.secret_number:
                st.session_state.feedback = "Too low!"
            elif guess > st.session_state.secret_number:
                st.session_state.feedback = "Too high!"
            else:
                st.success(f"🎉 Correct! The number was {st.session_state.secret_number}.")
                st.success(f"✅ Guessed in {st.session_state.attempts} attempts.")
                if st.button("🔁 Play Again"):
                    for key in ["secret_number", "guess", "attempts", "feedback", "locked"]:
                        del st.session_state[key]
                    st.experimental_rerun()

        st.write(f"🔁 Attempts: {st.session_state.attempts}")
        if st.session_state.feedback:
            st.warning(st.session_state.feedback)
