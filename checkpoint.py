import streamlit as st
import io
import contextlib
from code_editor import code_editor
from utils.db import save_quiz_result

def show():
    if "score" not in st.session_state:
        st.session_state.score = 0
        st.session_state.quiz_completed = False
    """Checkpoint page with interactive coding challenges."""

    st.header("The Checkpoint")

    st.write(
        "You've come far! Well done. But now is the time to put your knowledge to the test."
    )

    st.caption("Sorry for the scrolling.")

    st.write("### How it works:")
    st.write("1. Read the question")
    st.write("2. Write/click your answer")
    st.write("3. Use the run button to test your code")

    # --- QUESTION 1 ---
    st.subheader("Question 1:")
    st.write("Fix the code so it prints 'monkey'.")

    btns = [{
        "name": "Run",
        "feather": "Play",
        "primary": True,
        "hasText": True,
        "commands": ["submit"],
        "style": {"bottom": "0.44rem", "right": "0.4rem"}
    }]

    initial_code = "enemy_type = 'monkey'\n# Write your code below\n"
    response = code_editor(initial_code, lang="python", buttons=btns)

    if response['type'] == "submit":
        user_code = response['text']
        output_buffer = io.StringIO()

        try:
            with contextlib.redirect_stdout(output_buffer):
                exec(user_code, {})

            printed_val = output_buffer.getvalue().strip()

            if printed_val == "monkey":
                st.success(f"Perfect! You printed: {printed_val}")
                st.session_state.score += 1
            elif printed_val == "":
                st.warning("Nothing printed. Did you use print()?") 
            else:
                st.error(f"Expected 'monkey' but got '{printed_val}'")

        except Exception as e:
            st.error(f"Execution Error: {e}")

        # --- QUESTION 2 ---
        user_guess4 = st.radio(
            "Question 2: Which is a string?",
            ["'I'm so good at coding'", "I'm so good at coding", "(i'm so good at coding)"],
            index=None,
            key="quiz4"
        )

        if user_guess4:
            if user_guess4 == "'I'm so good at coding'":
                st.success("Correct!")
                st.session_state.score += 1
            else:
                st.error("Not quite.")

            # --- QUESTION 3 ---
            user_guess5 = st.radio(
                "Question 3: Can print() add numbers?",
                ["True", "False"],
                index=None,
                key="quiz5"
            )

            if user_guess5:
                if user_guess5 == "True":
                    st.success("Correct!")
                    st.session_state.score += 1
                else:
                    st.error("Incorrect!")

                # --- QUESTION 4 ---
                user_guess6 = st.radio(
                    "Question 4: Multiplication symbol?",
                    ["`x`", "`**`", "`*`", "`%`"],
                    index=None,
                    key="quiz6"
                )

                if user_guess6:
                    if user_guess6 == "`*`":
                        st.success("Correct!")
                        st.session_state.score += 1
                    else:
                        st.error("Wrong symbol.")

                    # --- QUESTION 5 ---
                    st.subheader("Question 5:")
                    st.write("Find the difference between scores.")

                    initial_code2 = (
                        "player1_score = 2124\n"
                        "player2_score = 1203\n"
                        "# Write your code below\n"
                    )

                    response2 = code_editor(initial_code2, lang="python", buttons=btns)

                    if response2['type'] == "submit":
                        user_code2 = response2['text']
                        output_buffer2 = io.StringIO()

                        try:
                            with contextlib.redirect_stdout(output_buffer2):
                                exec(user_code2, {})

                            printed_val2 = output_buffer2.getvalue().strip()

                            if printed_val2 == "921":
                                st.success(f"Perfect! You printed: {printed_val2}")
                                st.session_state.score += 1
                            elif printed_val2 == "":
                                st.warning("Nothing printed.")
                            else:
                                st.error(f"Got '{printed_val2}', not correct.")

                        except Exception as e2:
                            st.error(f"Execution Error: {e2}")

                        st.divider()
                        st.write("Nice work. You've covered the basics.")


                        if not st.session_state.quiz_completed:
                            current_user = st.session_state.username
                            total_questions = 5  

                            save_quiz_result(
                            username=current_user,
                            score=st.session_state.score,
                            total=total_questions
                            )
    
                            st.session_state.quiz_completed = True
                            st.rerun()  # refresh to show success message

                            if st.session_state.quiz_completed:
                                st.success(f"Quiz complete! Your score {st.session_state.score}/{total_questions} saved.")