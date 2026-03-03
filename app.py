import streamlit as st

st.set_page_config(page_title="The Python Project", page_icon="🐍")
st.title("🐍 Python Learning Path")

if "nav_key" not in st.session_state:
    st.session_state["nav_key"] = "Home Page"

def welcome():
    st.header("Welcome to my Python Course!")
    st.write("This website is to teach you some python.")
    name = st.text_input("What's your name?")
    if name:
        st.success(f"Hi {name}. Time to start coding.")

st.sidebar.title("Lessons")

the_page = st.sidebar.radio("Go to:", ["Home Page", "The basics", "Week 2"], key = "nav_key")

page_map = {"Home Page": 0, "The basics": 1, "Week 2": 2}
current_step = page_map.get(the_page, 0)
total_steps = len(page_map) - 1
if current_step > 0:
    progress_float = float(current_step / total_steps)
    super_progress_epic = max(0.0, min(progress_float, 1.0))
    
    st.sidebar.write(f"**Course Progress: {int(super_progress_epic * 100)}%**")
    st.sidebar.progress(super_progress_epic)
else:
    st.sidebar.write("**Course Progress: 0%**")
    st.sidebar.progress(0.0)    

if the_page == "Home Page":
    welcome()
    st.divider()
    st.markdown("## Why use python?")
    st.subheader("The popularity of the biggest languages (%)")
    st.write("The rest of the languages are not shown, but are the remaining 36% not shown on the cool graph.")

    chart_data_cool = {"Python": 25, "Java": 21, "JavaScript": 8, "C#": 7}
    st.bar_chart(chart_data_cool)
    st.markdown("Source: [https://www.statista.com/chart/16567/popular-programming-languages/?srsltid=AfmBOooCo-F7T61EWQEkaASlvtsIwpnGKq-qA1K0hLLP64Fs3VogekTE]")
    what_u_can_do, another_one =st.columns(2)
    with what_u_can_do:
        st.subheader("What can you do with python?")
        st.image("https://f4.bcbits.com/img/a2712205983_16.jpg")
    with another_one:
        st.subheader("...a lot of stuff")
        st.write("Python is a very diverse language, allowing you to do a bunch of stuff:")
        st.markdown("-Web development")
        st.markdown("-App development")
        st.markdown("-Creating AI")
        st.markdown("-Game development")
        st.markdown("-And much more!")


elif the_page == "The basics":
    basics, strings, integers, syntax_errors, variables = st.tabs(["Basics", "Strings", "Integers", "Syntax Errors", "Variables"])
    basics.header("Week 1: The Basics") 
    basics.info("Here, you will learn about the absolute basics of Python, like syntax, variables, and different data types. This is basics of Python.")
    strings.header("Strings")
    strings.write("Here is a simple example of Python code:")
    strings.code("print('Hello, World!')")
    strings.write("Lets break down this code:" \
    "`print()` is a function that outputs text to the console." \
    "`'Hello, World!'` is a string, represents text (normal writing). In this case, it will display the message 'Hello, World!' when the code is run.")
    strings.write("Notice how `'Hello, World!'` is surrounded by quotation marks? Thats how Python knows its not a variable or function, allowing you to write whatever you want in there without the console getting confused.")
    user_guess = strings.radio("Which option here is a string?", ["42", "hi!", "'Hello!'"], index = None, key = "quiz1")
    if user_guess:
        if user_guess == "'Hello!'":
            strings.success("Yeah, 'Hello!' is a string because it is surrounded by quotation marks.")
        elif user_guess is not None:
            strings.error("Close. A string is a something that is surrounded by quotation marks.")
    st.divider()
    user_guess2 = strings.radio("What are strings surrounded by?", ["brackets", "quotation marks", "parentheses", "Only the '' marks"], index = None, key = "quiz2")
    if user_guess2:
        if user_guess2 == "quotation marks":
            strings.success("Right! Strings are surrounded by quotations, which can be (' ') or (\" \")")
        elif user_guess2 is not None:
            strings.error("While single quotation marks (' ') can be used to make strings, double ones (\" \") can also be used.")
    strings.subheader("Summary")
    strings.write("So, strings must be surrounded by quotations, and can have anything you want in there. They are used to represent text, like the ones your actually reading right now.")
    strings.write("If you want to have a string to actually appear where you want it to, for example the console, you would need to use the `print()` function. More on that later.")
    strings.write("Therefore, you can use strings for a variety of purposes, but its all up to you.")
    strings.code("print('Well done on completing your first lesson.')")
elif the_page == "Week 2":
    st.header("Week 2: Data Types")
    st.info("Coming soon: Learn about different data types in Python!")
