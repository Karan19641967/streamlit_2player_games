import streamlit as st

def tic_tac_toe():
    st.title("❌🟢 Tic Tac Toe (2 Players)")

    if "board" not in st.session_state:
        st.session_state.board = [""] * 9
        st.session_state.current_player = "X"
        st.session_state.winner = None

    def check_winner():
        b = st.session_state.board
        wins = [(0,1,2), (3,4,5), (6,7,8), (0,3,6),
                (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
        for i, j, k in wins:
            if b[i] == b[j] == b[k] and b[i] != "":
                return b[i]
        if "" not in b:
            return "Draw"
        return None

    cols = st.columns(3)
    for i in range(3):
        for j in range(3):
            idx = i * 3 + j
            with cols[j]:
                if st.button(st.session_state.board[idx] or " ", key=idx):
                    if st.session_state.board[idx] == "" and st.session_state.winner is None:
                        st.session_state.board[idx] = st.session_state.current_player
                        st.session_state.winner = check_winner()
                        if st.session_state.winner is None:
                            st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"

    if st.session_state.winner:
        if st.session_state.winner == "Draw":
            st.warning("It's a draw!")
        else:
            st.success(f"🎉 {st.session_state.winner} wins!")
        if st.button("🔁 Play Again"):
            st.session_state.board = [""] * 9
            st.session_state.current_player = "X"
            st.session_state.winner = None
