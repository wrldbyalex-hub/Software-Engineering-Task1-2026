import streamlit as st
import io
import contextlib
from code_editor import code_editor
from utils.db import save_quiz_result

def show():
    """Checkpoint page with different coding questions and challenges"""
    if "score" not in st.session_state:
        st.session_state.score = 0
    if "quiz_completed" not in st.session_state: # these will check if the question is answered
        st.session_state.quiz_completed = False
    if "q1_submitted" not in st.session_state: # if it is, the next question will show
        st.session_state.q1_submitted = False
    if "q2_submitted" not in st.session_state: # Otherwise they won't until the current question is answered 
        st.session_state.q2_submitted = False
    if "q3_submitted" not in st.session_state:
        st.session_state.q3_submitted = False
    if "q4_submitted" not in st.session_state:
        st.session_state.q4_submitted = False
    if "q5_submitted" not in st.session_state:
        st.session_state.q5_submitted = False
    if "correct_questions" not in st.session_state:
        st.session_state.correct_questions = set() # checks if the key correct question already exists 
        # if no it creates a new set and stores the data there
        # if yes it does nothing and keeps whatever value is already there 

    st.header("The Checkpoint")
    st.write("You've come far! Well done. But now is the time to put your knowledge to the test.")
    st.caption("Sorry for the scrolling.")
    st.write("### How it works:")
    st.write("1. Read the question")
    st.write("2. Write/click your answer")
    st.write("3. Submit / Run to check")
    st.write("Submit any answer to unlock the next question (correct or not).")

    # Q1 always visible
    st.subheader("Question 1:")
    st.write("Fix the code so it prints 'monkey'.")
    btns = [{"name": "Run", "feather": "Play", "primary": True, "hasText": True, "commands": ["submit"], "style": {"bottom": "0.44rem", "right": "0.4rem"}}]
    initial_code = "enemy_type = 'monkey'\n# Write your code below\n"
    response = code_editor(initial_code, lang="python", buttons=btns, key="q1_editor")

    if response['type'] == "submit" and not st.session_state.q1_submitted:
        user_code = response['text']
        output_buffer = io.StringIO()
        # Safe environment - no access to dangerous builtins or modules
        safe_globals = {
            "__builtins__": {},          
            "print": print
        }

        try:
            with contextlib.redirect_stdout(output_buffer):
                exec(user_code, safe_globals)
            printed_val = output_buffer.getvalue().strip()
            if printed_val == "monkey" and 1 not in st.session_state.correct_questions:
                st.success(f"Perfect! You printed: {printed_val}")
                st.session_state.score += 1 # adds the question to the correct questions section
                st.session_state.correct_questions.add(1) # marks question as correct
            elif printed_val == "":
                st.warning("Nothing printed. Did you use print()?")
            else:
                st.error(f"Expected 'monkey' but got '{printed_val}'")
            st.session_state.q1_submitted = True
            st.rerun()
        except Exception as e:
            st.error(f"Execution Error: {e}")

    # Q2 shows after Q1 submitted
    if st.session_state.q1_submitted:
        st.subheader("Question 2:")
        user_guess4 = st.radio(
            "Which is a string?",
            ["'I'm so good at coding'", "I'm so good at coding", "(i'm so good at coding)"],
            index=None,
            key="quiz4"
        )
        if user_guess4 and not st.session_state.q2_submitted:
            if user_guess4 == "'I'm so good at coding'":
                st.success("Correct!")
                st.session_state.score += 1
                st.session_state.correct_questions.add(2)
            else:
                st.error("Not quite.")
            st.session_state.q2_submitted = True
            st.rerun()

    # Q3 after Q2 submitted
    if st.session_state.q2_submitted:
        st.subheader("Question 3:")
        user_guess5 = st.radio(
            "Can print() add numbers?",
            ["True", "False"],
            index=None,
            key="quiz5"
        )
        if user_guess5 and not st.session_state.q3_submitted:
            if user_guess5 == "True":
                st.success("Correct!")
                st.session_state.score += 1
                st.session_state.correct_questions.add(3)
            else:
                st.error("Incorrect!")
            st.session_state.q3_submitted = True
            st.rerun()

    # Q4 after Q3
    if st.session_state.q3_submitted:
        st.subheader("Question 4:")
        user_guess6 = st.radio(
            "Multiplication symbol?",
            ["`x`", "`**`", "`*`", "`%`"],
            index=None,
            key="quiz6"
        )
        if user_guess6 and not st.session_state.q4_submitted:
            if user_guess6 == "`*`":
                st.success("Correct!")
                st.session_state.score += 1
                st.session_state.correct_questions.add(4)
            else:
                st.error("Wrong symbol.")
            st.session_state.q4_submitted = True
            st.rerun()

    # Q5 after Q4
    if st.session_state.q4_submitted:
        st.subheader("Question 5:")
        st.write("Find the difference between scores and print it to the console.")
        initial_code2 = "player1_score = 2124\nplayer2_score = 1203\n# Write your code below\n"
        response2 = code_editor(initial_code2, lang="python", buttons=btns, key="q5_editor")

        if response2['type'] == "submit" and not st.session_state.q5_submitted:
            user_code2 = response2['text']
            output_buffer2 = io.StringIO()
            try:
                with contextlib.redirect_stdout(output_buffer2):
                    exec(user_code2, {})
                printed_val2 = output_buffer2.getvalue().strip()
                if printed_val2 == "921" and 5 not in st.session_state.correct_questions:
                    st.success(f"Perfect! You printed: {printed_val2}")
                    st.session_state.score += 1
                    st.session_state.correct_questions.add(5)
                elif printed_val2 == "":
                    st.warning("Nothing printed.")
                else:
                    st.error(f"Got '{printed_val2}', not correct.")
                st.session_state.q5_submitted = True
                st.rerun()
            except Exception as e2:
                st.error(f"Execution Error: {e2}")

    st.divider()

    # Finish button after Q5 submitted
    if st.session_state.q5_submitted and not st.session_state.quiz_completed:
        if st.button("Finish & Save Quiz", type="primary"):
            current_user = st.session_state.username
            total_questions = 5
            save_quiz_result(username=current_user, score=st.session_state.score, total=total_questions)
            st.session_state.quiz_completed = True
            st.rerun()

    if st.session_state.quiz_completed:
        st.success(f"Quiz complete! Your score {st.session_state.score}/5 has been saved.")