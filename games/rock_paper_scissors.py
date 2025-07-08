import streamlit as st

def rock_paper_scissors():
    st.title("🪨📄✂️ Rock Paper Scissors - 2 Player Mode")

    options = ["Rock", "Paper", "Scissors"]

    # Game state setup
    if "player1_choice" not in st.session_state:
        st.session_state.player1_choice = None
    if "player2_choice" not in st.session_state:
        st.session_state.player2_choice = None
    if "result_shown" not in st.session_state:
        st.session_state.result_shown = False

    # Player 1 input
    with st.expander("Player 1 - Make your choice"):
        st.session_state.player1_choice = st.radio("Player 1:", options, key="p1")

    # Player 2 input
    with st.expander("Player 2 - Make your choice"):
        st.session_state.player2_choice = st.radio("Player 2:", options, key="p2")

    # Compare choices
    def decide_winner(p1, p2):
        if p1 == p2:
            return "It's a draw!"
        elif (p1 == "Rock" and p2 == "Scissors") or \
             (p1 == "Paper" and p2 == "Rock") or \
             (p1 == "Scissors" and p2 == "Paper"):
            return "🎉 Player 1 wins!"
        else:
            return "🎉 Player 2 wins!"

    # Show result
    if st.button("Play"):
        if st.session_state.player1_choice and st.session_state.player2_choice:
            result = decide_winner(st.session_state.player1_choice, st.session_state.player2_choice)
            st.success(result)
            st.session_state.result_shown = True
        else:
            st.warning("Both players must make a choice!")

    # Reset button
    if st.session_state.result_shown and st.button("🔁 Play Again"):
        st.session_state.player1_choice = None
        st.session_state.player2_choice = None
        st.session_state.result_shown = False
        st.experimental_rerun()
