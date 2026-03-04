from code_editor import code_editor
import streamlit as st

st.set_page_config(page_title="The Python Project", page_icon="🐍") # Would be related to the link if there was one.
st.title("🐍 Python Learning Path") # The title of the page.

if "nav_key" not in st.session_state: 
    st.session_state["nav_key"] = "Home Page" # This is to make sure that when using the sidebar buttons, the page doesn't reset to the home page.

def welcome(): # This function is to make the name input able to accept any name and then return that value back to welcome for later use.
    st.header("Welcome to my Python Course!")
    st.write("This website is to teach you some python.")
    name = st.text_input("What's your name?")
    if name:
        st.success(f"Hi {name}. Time to start coding.")

st.sidebar.title("Lessons") 

the_page = st.sidebar.radio("Go to:", ["Home Page", "The basics", "Detailed Variables"], key = "nav_key") # The sidebar Buttons and the key for streamlit to recognise them.

page_map = {"Home Page": 0, "The basics": 1, "Detailed Variables": 2} # percentage bar because i thought it would be cool. I used floats to make the percentage calculationns easier to read.
current_step = page_map.get(the_page, 0)
total_steps = len(page_map) - 1 # used len to make it so if I add more pages it will automatically update the total steps.
if current_step > 0: # Makes it so that the percentage bar only moves when you move tabs
    progress_float = float(current_step / total_steps) # Math
    super_progress_epic = max(0.0, min(progress_float, 1.0))
    
    st.sidebar.write(f"**Course Progress: {int(super_progress_epic * 100)}%**")
    st.sidebar.progress(super_progress_epic)
else: # To make it so that the percentage bar is at 0% when your on the home page as your not learning anything fr.
    st.sidebar.write("**Course Progress: 0%**")
    st.sidebar.progress(0.0) 

if the_page == "Home Page": # Home page
    welcome()
    st.divider()
    st.markdown("## Why use python?") # the ## is to affect the size.
    st.subheader("The popularity of the biggest languages (%)")
    st.write("The rest of the languages are not shown, but are the remaining 36% not shown on the cool graph.") 

    chart_data_cool = {"Python": 25, "Java": 21, "JavaScript": 8, "C#": 7} # data chart showing which coding languages are used the most, as well as a source for where the data is from.
    st.bar_chart(chart_data_cool)
    st.markdown("Source: [https://www.statista.com/chart/16567/popular-programming-languages/?srsltid=AfmBOooCo-F7T61EWQEkaASlvtsIwpnGKq-qA1K0hLLP64Fs3VogekTE]")
    what_u_can_do, another_one =st.columns(2) # columns to make the page look nicer and less cluttered, allowing for more content to be shown without it looking bad. Not only does this contrast the page, 
    with what_u_can_do: # but it also allows for it to be more organised.
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
        st.markdown("*Streamlit* is **really** ***cool***.")
        st.markdown('''
            :red[As you] :orange[can see,] :green[Python can] :blue[do some] :violet[really cool]
            :gray[stuff as] :rainbow[shown above.]''') # aestheticaly pleasing for me, nothing much here lol
    st.divider()
    st.subheader("Just remember that this is the **basics**. Kinda.")

# This is the first page. It has quite alot of content, so I used tabs to make it look nicer, and also its more organised, because if you just have one page thats alot of scrolling.
# I also added some questions to make sure the user understands the code and concepts, because like if you read it but don't implement it, your gonna forget it.
elif the_page == "The basics": 
    basics, strings, integers, variables, test1 = st.tabs(["Basics", "Strings", "Integers", "Variables", "Test"])
    basics.header("Welcome to The Basics") 
    basics.info("Here, you will learn about the absolute basics of Python, like syntax, variables, and different data types. This is basics of Python.")
    basics.write("Python is probably the best programming language to start with, because it reads a lot like english, and can be used for a wide variety of things.")
    string_basics = basics.expander("Strings") # expanders to make the page look nicer and less cluttered. They can also hold information, so that its more interactive. I like that.
    string_basics.write('''A string is anything surrounded in either (" "), or (' '). Go to the strings tab to learn more about strings and how they work.''')
    integers_basics = basics.expander("Integers")
    integers_basics.write('''An integer is a whole number, positive or negative, WITHOUT decimals.''')
    variables_basics = basics.expander("Variables")
    variables_basics.write('''A variable is a way to store information, like a container. You can put anything in there, and then use it later on in your code. For example, you could have a variable called `name` and store your name in there, and then use that variable to print your name later on. Oh wait, I did that.''')
    
    strings.header("Strings")
    strings.write("Here is a simple example of Python code:")
    strings.code("print('Hello, World!')") 
    strings.write("Lets break down this code: "
    "`print()` is a function that outputs text to the console. "
    "`'Hello, World!'` is a string, represents text (normal writing). In this case, it will display the message 'Hello, World!' when the code is run.")
    strings.write("Notice how `'Hello, World!'` is surrounded by quotation marks? Thats how Python knows its not a variable or function, allowing you to write whatever you want in there without the console getting confused.")
    user_guess = strings.radio("Which option here is a string?", ["42", "hi!", "'Hello!'"], index = None, key = "quiz1") # The index = None is to make it so that the question isn't auto answered.
    if user_guess: # This if statement is to make sure that the user has actually made a guess, and not just do nothing like a bum.
        if user_guess == "'Hello!'":
            strings.success("Yeah, 'Hello!' is a string because it is surrounded by quotation marks.")
        elif user_guess is not None: # if the answer is anything BUT the right answer, it will show this message. The reason I used elif instead of else is to make it so that if the user hasn't made a guess, it won't show the error message, because that would be annoying.
            strings.error("Close. A string is a something that is surrounded by quotation marks.")
    st.divider() # divider to make the page look nicer and less cluttered.
    user_guess2 = strings.radio("What are strings surrounded by?", ["brackets", "quotation marks", "parentheses", "Only the '' marks"], index = None, key = "quiz2")
    if user_guess2: # Same for this question, to make sure the user has made a guess.
        if user_guess2 == "quotation marks":
            strings.success("Right! Strings are surrounded by quotations, which can be (' ') or (\" \")")
        elif user_guess2 is not None: # same here tbh
            strings.error("While single quotation marks (' ') can be used to make strings, double ones (\" \") can also be used.") # Didn't mention this earlier
    strings.subheader("Summary")
    strings.write("So, strings must be surrounded by quotations, and can have anything you want in there. They are used to represent text, like the ones your actually reading right now.")
    strings.write("If you want to have a string to actually appear where you want it to, for example the console, you would need to use the `print()` function. More on that later.")
    strings.write("Therefore, you can use strings for a variety of purposes, but its all up to you.")
    strings.code("print('Well done on completing your first lesson.')")
    
    integers.header("Integers")
    integers.write("As you probably know, integers are whole numbers, positive or negative. They can be used for a bunch of things, like doing simple math, or even advanced math. However, unlike " \
    "strings, integers can't be used to represent text, and you probably shouldn't surround them in quotation marks." \
    "for example:")
    integers.code("print(42)")
    integers.write("This will print the number 42 to the console. However, if you put it in quotation marks, like this:")
    integers.code("print('42')")
    integers.write("It will print the string '42', which isn't a number.")
    user_guess3 = integers.radio("Which one here is a integer?", ["42", "'42'", "Both of them"], index = None, key = "quiz3")
    if user_guess3: # Do I need to explain?
        if user_guess3 == "42":
            integers.success("Right! 42 is an integer because it is a whole number.")
        elif user_guess3 is not None:
            integers.error("Not quite my tempo.")
    integers.subheader("More things you can do with Integers")
    integers.write("As mentioned before, you can do math.")
    integers.code("print(2 + 2)")
    integers.write("This will print 4, because 2 + 2 = 4.")
    integers.write("But thats just the start. But before you learn more, you'll need to know this:")
    different_math_things = { # This is the start of a table to show different math signs and what they do
        "Sign": ["`+`", "`-`", "`*`", "`/`", "`**`", "`%`"], # surrounded in `` because the console thought it was a list when I didn't want it to, so this is a easy fix.
        "Name": ["Addition", "Subtraction", "Multiplication", "Division", "Exponentiation", "Modulo"], # The names that will apear next to the signs
        "Purpose": [ # What they do and stuff
            "Adding two numbers together",
            "Subtracting one number from another",
            "Multiplying two numbers together",
            "Dividing one number by another",
            "Raising a number to the power of another",
            "Finding the remainder after division"
        ],
        "example": [ # A example of how to use the sign and what it does.
            "print(2 + 2) # This will print 4",
            "print(5 - 3) # This will print 2",
            "print(4 * 3) # This will print 12",
            "print(10 / 2) # This will print 5.0",
            "print(2 ** 3) # This will print 8",
            "print(10 % 3) # This will print 1"
        ]
    }
    integers.table(different_math_things) # A table to show the different math signs, their names, purposes, and examples. I think this is a good way to show this information, because its easy to read and understand.
    integers.write("As you can see, there are a lot of different math signs, and they all have different purposes.")
    integers.code("print('Well done again on completing another section.')")
    
    variables.header("Variables")
    variables.write("Variables are what you store information in. You can put anything in there, and then use it later. For example, you could have \
                    a variable called `coolguy` and store the string 'Alex' in there, and then use that variable to print it later on.")
    variables.code("coolguy = 'Alex'\nprint(coolguy)")
    variables.write("This will print 'Alex' to the console, because we stored that string in the variable `coolguy`. You can also store integers in variables, like this:")
    variables.code("age = 16\nprint(age)")
    variables.write("This will print 16 to the console, because we stored that integer in the variable `age`. You can also do cool things in a variable, like this:")
    variables.code("alex_score = 17\nxavier_score = 20\nprint(alex_score + xavier_score)")
    variables.write("This will print 37 to the console, because we stored the integers 17 and 20 in the variables, and just added them together like boom.")
    container = variables.container(border = True)
    container.subheader("Examples of variables")
    container.code("player_health = 1000\narmour_multiplier = 2\narmoured_health = player_health * armour multiplier\nprint(armoured_health)")
    container.write("**Console:** 2000")
    container.divider()
    container.code("best_sword = 'Katana'\nprint(best_sword)")
    container.write("**Console:** Katana")
    container.code("sentence_start = 'You have'\nsentence_end = Health'\n\nplayer1_health = '1200'\nplayer2_health = '1100'\n\nprint(sentence_start + player1_health + sentence_end)\nprint(sentence_start + player2_health + sentence_end)")
    container.write("**Console:** You have 1200 Health.")
    container.write("**Console:** You have 1100 Health.")
    container.divider()
    container.write("Note: When making a variable with multiple words, you MUST use a _ (underscore) to connect those words, otherwise the console will do a flip and freak out.")

    test1.header("The Checkpoint")
    test1.write("You've come far! Well done. But now is the time to put your knowledge to the test. Hopefully you get it all right," \
    "and feel free to re-attempt any Questions, thats why they are still editable after getting it wrong/right.")
    test1.write("It works like this: They code already there will be OUTSIDE the box, while what you need to write will need to be inside the box.")
    test1.subheader("Question 1:")
    test1.write("The Game Fantasy Quest wants their variable enemy_type to equal 'monkey', but can't figure out why it won't print to the console. Use the space below to fix their code.")
    initial_code = "enemy_type = 'monkey'\n#fix the code below this line\n"
    response = code_editor(initial_code, lang = "python", key = "Question1")
    if test1.button("Run code"):
        raw_code = response["text"]
        normalised_code = raw_code.replace(" ", "").replace("\n", "").strip()
        if "print(enemy_type)" in normalised_code: 
            test1.success("Correct. Well done!")
        elif "print('enemy_type')" in normalised_code or 'print("enemy_type")' in normalised_code:
            test1.error("Close! But you put quotes around enemy_type. That tells Python to print the *word* 'enemy_type' instead of the variable's *value*.")
        else:
            test1.error("Almost! Check your code. You need to print enemy_type. Remember, python is case sensitive. Enemy_type is not the same as enemy_type.")
        
        

# Week 2, should start this I think, probably not going to be about data types, despite that devious name. Edit: I changed it, rip data types.
elif the_page == "Detailed Variables":
    st.header("Week 2: Detailed Variables")
    st.info("Coming soon: Learn about more variables in Python!")
