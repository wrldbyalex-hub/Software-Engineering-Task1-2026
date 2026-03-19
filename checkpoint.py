import streamlit as st
import io
import contextlib
from code_editor import code_editor
from utils.db import save_quiz_result

def show():
    """Checkpoint page with interactive coding challenges."""
    # Init state
    if "score" not in st.session_state: # checks if questions have been answered. If not, it creates them and starts counting.
        st.session_state.score = 0
    if "quiz_completed" not in st.session_state:
        st.session_state.quiz_completed = False
    if "q1_correct" not in st.session_state:
        st.session_state.q1_correct = False
    if "q2_correct" not in st.session_state:
        st.session_state.q2_correct = False
    if "q3_correct" not in st.session_state:
        st.session_state.q3_correct = False
    if "q4_correct" not in st.session_state:
        st.session_state.q4_correct = False
    if "q5_correct" not in st.session_state:
        st.session_state.q5_correct = False

    st.header("The Checkpoint")
    st.write("You've come far! Well done. But now is the time to put your knowledge to the test.")
    st.caption("Sorry for the scrolling.")
    st.write("### How it works:")
    st.write("Answer correctly to unlock the next question. You results will be displayed once you answer all questions.")

# --- Question 1 ----------
    # Q1 always shown 
    st.subheader("Question 1:")
    st.write("Fix the code so it prints 'monkey'.")
    btns = [{"name": "Run", "feather": "Play", "primary": True, "hasText": True, "commands": ["submit"], "style": {"bottom": "0.44rem", "right": "0.4rem"}}]
    initial_code = "enemy_type = 'monkey'\n# Write your code below\n"
    response = code_editor(initial_code, lang="python", buttons=btns, key="q1_editor")

    if response['type'] == "submit" and not st.session_state.q1_correct: # updated with q1 
        user_code = response['text']
        output_buffer = io.StringIO()
        try: # string buffer to capture whatever code they entered 
            with contextlib.redirect_stdout(output_buffer):
                exec(user_code, {})
            printed_val = output_buffer.getvalue().strip()
            if printed_val == "monkey":
                st.success(f"Perfect! You printed: {printed_val}")
                st.session_state.score += 1
                st.session_state.q1_correct = True
                st.rerun()
            elif printed_val == "":
                st.warning("Nothing printed. Did you use print()?")
            else:
                st.error(f"Expected 'monkey' but got '{printed_val}'")
        except Exception as e:
            st.error(f"Execution Error: {e}")

# --- Question 2 ----------
    # Q2 only if Q1 correct
    if st.session_state.q1_correct:
        st.subheader("Question 2:")
        user_guess4 = st.radio(
            "Which is a string?",
            ["'I'm so good at coding'", "I'm so good at coding", "(i'm so good at coding)"],
            index=None,
            key="quiz4"
        )
        if user_guess4 and not st.session_state.q2_correct:
            if user_guess4 == "'I'm so good at coding'":
                st.success("Correct!")
                st.session_state.score += 1
                st.session_state.q2_correct = True
                st.rerun()
            else:
                st.error("Not quite.")

# --- Question 3 -----------
    # Q3 only if Q2 correct
    if st.session_state.q2_correct:
        st.subheader("Question 3:")
        user_guess5 = st.radio(
            "Can print() add numbers?",
            ["True", "False"],
            index=None,
            key="quiz5"
        )
        if user_guess5 and not st.session_state.q3_correct:
            if user_guess5 == "True":
                st.success("Correct!")
                st.session_state.score += 1
                st.session_state.q3_correct = True
                st.rerun()
            else:
                st.error("Incorrect!")

# --- Question 4 -----------
    # Q4 only if Q3 correct
    if st.session_state.q3_correct:
        st.subheader("Question 4:")
        user_guess6 = st.radio(
            "Multiplication symbol?",
            ["`x`", "`**`", "`*`", "`%`"],
            index=None,
            key="quiz6"
        )
        if user_guess6 and not st.session_state.q4_correct:
            if user_guess6 == "`*`":
                st.success("Correct!")
                st.session_state.score += 1
                st.session_state.q4_correct = True
                st.rerun()
            else:
                st.error("Wrong symbol.")

# --- Question 5 ------------
    # Q5 only if Q4 correct
    if st.session_state.q4_correct:
        st.subheader("Question 5:")
        st.write("Find the difference between scores.")
        initial_code2 = "player1_score = 2124\nplayer2_score = 1203\n# Write your code below\n"
        response2 = code_editor(initial_code2, lang="python", buttons=btns, key="q5_editor")

        if response2['type'] == "submit" and not st.session_state.q5_correct:
            user_code2 = response2['text']
            output_buffer2 = io.StringIO()
            try: # creates a string buffer to get the output 
                with contextlib.redirect_stdout(output_buffer2):
                    exec(user_code2, {})
                printed_val2 = output_buffer2.getvalue().strip() # Removes empty spaces 
                if printed_val2 == "921":
                    st.success(f"Perfect! You printed: {printed_val2}")
                    st.session_state.score += 1
                    st.session_state.q5_correct = True
                    st.rerun()
                elif printed_val2 == "":
                    st.warning("Nothing printed.")
                else:
                    st.error(f"Got '{printed_val2}', not correct.")
            except Exception as e2:
                st.error(f"Execution Error: {e2}")

    st.divider()

    # Show finish button only when Q5 correct
    if st.session_state.q5_correct and not st.session_state.quiz_completed:
        if st.button("Finish & Save Quiz", type="primary"):
            current_user = st.session_state.username
            total_questions = 5
            save_quiz_result(username=current_user, score=st.session_state.score, total=total_questions)
            st.session_state.quiz_completed = True
            st.rerun()

    if st.session_state.quiz_completed:
        st.success(f"Quiz complete! Your score {st.session_state.score}/5 has been saved.")