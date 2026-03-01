import streamlit as st

# trying to make the question save
if "quiz done" not in st.session_state:
    st.session_state["quiz done"] = False
    
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
the_page = st.sidebar.radio("Go to:", ["Home Page", "The basics", "Week 2", "Week 3", "Week 4"])

if the_page == "Home Page":
    welcome()

elif the_page == "The basics":
    st.header("Week 1: The Basics")
    st.info("In this stage, you will learn about the absolute basics of Python, including syntax, variables, and simple data types. This is the foundation for your Python journey!")
    st.write("Here is a simple example of Python code:")
    st.code("print('Hello, World!)")
    st.write("Lets break down this code:" \
    "`print()` is a function that outputs text to the console." \
    "`'Hello, World!'` is a string, represents text (normal writing). In this case, it will display the message 'Hello, World!' when the code is run.")
    st.write("Notice how `'Hello, World!'` is surrounded by quotation marks? Thats how Python knows its not a variable or function, allowing you to write whatever you want in there without the console getting confused.")
    user_guess =st.radio("Question: Which option here is a string?", ["42", "hi!", "'Hello!'"])
    if user_guess == "'Hello!'":
        st.session_state["quiz done"] = True
        st.success("Correct! 'Hello!' is a string because it is enclosed in quotation marks.")
    else:
        st.error("Not quite. Remember, a string is a sequence of characters enclosed in quotation marks. Try again!")

elif the_page == "Week 2":
    st.header("Week 2: Data Types")
    st.info("Coming soon: Learn about different data types in Python!")
