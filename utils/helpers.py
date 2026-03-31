import streamlit as st

def show_home_content():
    """Displays the home page content."""
    st.divider()
    st.markdown("## Why use python?")
    st.subheader("The popularity of the biggest languages (%)")

    chart_data = {"Python": 25, "Java": 21, "JavaScript": 8, "C#": 7}
    st.bar_chart(chart_data)

    col1, col2 = st.columns(2) # columns help with the look and also are better for bigger screens 

    with col1:
        st.subheader("What can you do with python?")
        st.markdown("- Web development\n- App development\n- AI Creation\n- Game Development\n- Data Science\n- Robotics\n- Task automation\n\n- Interactive tools\n- and so much more.")