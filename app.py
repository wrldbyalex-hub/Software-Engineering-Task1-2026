import streamlit as st

# SECTION 4 REQUIREMENT: Function
def welcome():
    st.header("Welcome to my Python Course!")
    st.write("This website is being to tell you the basics of python.")
    name = st.text_input("First, what is your name?")
    if name:
        st.success(f"Hi {name}! Let's get started, and Good luck.")

# SECTION 1 REQUIREMENT: Navigation
st.set_page_config(page_title="Alex's Python Project", page_icon="🐍")
st.title("🐍 Python Learning Path")

# Sidebar for organization
st.sidebar.title("Course Map")
the_page = st.sidebar.radio("Go to:", ["Home Page", "Storing Data", "Week 2", "Week 3", "Week 4"])

if the_page == "Home Page":
    welcome()

elif the_page == "Week 1":
    st.header("Week 1: Variables")
    st.info("Coming soon: Learn how to store data!")
