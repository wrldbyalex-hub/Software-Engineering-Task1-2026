import streamlit as st

if "nav_key" not in st.session_state:
    st.session_state["nav_key"] = "Home Page"

# SECTION 1 REQUIREMENT: Navigation
st.set_page_config(page_title="Alex's Python Project", page_icon="🐍")
st.title("🐍 Python Learning Path")
# trying to make the question save
if "quiz done" not in st.session_state:
    st.session_state["quiz done"] = False

if st.session_state["quiz done"]:
        st.info("🌟 You've already completed this Question.")

st.write(f"DEBUG: Is the quiz done? {st.session_state['quiz done']}")
    
# SECTION 4 REQUIREMENT: Function
def welcome():
    st.header("Welcome to my Python Course!")
    st.write("This website is being to tell you the basics of python.")
    name = st.text_input("First, what is your name?")
    if name:
        st.success(f"Hi {name}! Let's get started, and Good luck.")

# Sidebar for organization
st.sidebar.title("Course Map")
the_page = st.sidebar.radio(
    "Go to:",
    ["Home Page", "The basics", "Week 2"]
    key="nav_key"
)

if the_page == "Home Page":
    welcome()

elif the_page == "The basics":
    st.header("Week 1: The Basics")
    if st.session_state["quiz done"]:
        st.info("🌟 You've already completed this Question.")
    st.info("In this stage, you will learn about the absolute basics of Python, including syntax, variables, and simple data types. This is the foundation for your Python journey!")
    st.write("Here is a simple example of Python code:")
    st.code("print('Hello, World!')")
    st.write("Lets break down this code:" \
    "`print()` is a function that outputs text to the console." \
    "`'Hello, World!'` is a string, represents text (normal writing). In this case, it will display the message 'Hello, World!' when the code is run.")
    st.write("Notice how `'Hello, World!'` is surrounded by quotation marks? Thats how Python knows its not a variable or function, allowing you to write whatever you want in there without the console getting confused.")
    user_guess = st.radio("Question: Which option here is a string?", ["42", "hi!", "'Hello!'"], index = None)
    if user_guess:
        if user_guess == "'Hello!'":
            st.success("Correct! 'Hello!' is a string because it is surrounded by quotation marks.")
            st.session_state["quiz done"] = True
        elif user_guess is not None:
            st.error("Close, but not there yet. A string is a something that is surrounded by quotation marks.")

elif the_page == "Week 2":
    st.header("Week 2: Data Types")
    st.info("Coming soon: Learn about different data types in Python!")
