import streamlit as st
from utils.db import get_user_quiz_history
def show():

    st.header("Goodbye")
    st.write("You have come quite a bit from 0 knowledge to this. I tried to make it so it was as simple as possible, and I hope I was able to do that for you.")
    st.write("But we're at the end now. You've finished the basics, but coding, Whether you think this is a good thing or not, coding never ends. There is always more you can learn- more you can do, and thats one of the beautiful things about it. ")
    st.write("Heres a little tease: F-strings. Functions. Syntax Errors. If you want to learn more, the first 3 chapters of a cool website called ***boot.dev*** will help you continue your learning path.")
    st.caption("You can always do it again though")

    st.subheader("Your Recent Quiz Results")
    history = get_user_quiz_history(st.session_state.username)
    if history:
        for row in history:
            ts, sc, tot, pct = row
            st.write(f"{ts} → {sc}/{tot} ({pct}%)")
    else:
        st.info("Complete a quiz to see your history!")
        
    st.subheader("Really cool button:")

    if "count" not in st.session_state:
        st.session_state.count = 0

    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:
        pass

    with col2:
        left, mid, right = st.columns([1, 3, 1])

        with mid:
            if st.button("Click me! 🔥", use_container_width=True, type="primary"):
                st.session_state.count += 1

    with col3:
        if st.button("Reset"):
            st.session_state.count = 0
            st.rerun()

    st.markdown(
        f"""
        <div style="
            text-align: center;
            font-size: 6rem;
            font-weight: bold;
            color: #00ff99;
            margin: 2rem 0;
            line-height: 1;
        ">
            {st.session_state.count}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='text-align: center; color: #aaaaaa; font-size: 1.2rem; margin-top: -1rem;'>"
        "times clicked</p>",
        unsafe_allow_html=True
    )

    if st.session_state.count >= 100:
        st.write("what are you doing bro")
    
    if st.session_state.count >= 200:
        st.write("This isn't the point of the website bro")