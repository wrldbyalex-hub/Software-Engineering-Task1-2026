import streamlit as st

# SECTION 4 REQUIREMENT: Function
def welcome_section():
    st.header("Welcome to the 4-Week Python Course!")
    st.write("This app is designed to help you learn coding from scratch.")
    name = st.text_input("First, what is your name?")
    if name:
        st.success(f"Hi {name}! Let's get started, and Good luck.")
        st.balloons()

# SECTION 1 REQUIREMENT: Navigation
st.set_page_config(page_title="Alex's Python Project", page_icon="🐍")
st.title("🐍 Python Learning Path")

# Sidebar for organization
st.sidebar.title("Course Map")
page = st.sidebar.radio("Go to:", ["Home Page", "Storing Data", "Week 2", "Week 3", "Week 4"])

if page == "Home Page":
    welcome_section()

elif page == "Week 1":
    st.header("Week 1: Variables")
    st.info("Coming soon: Learn how to store data!")
