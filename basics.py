import streamlit as st

def show():
    """Basics lesson page."""

    # Creates tabs for that page, all clickable
    basics, strings, integers, variables = st.tabs(["Basics", "Strings", "Integers", "Variables"]) #
    basics.header("Welcome to The Basics") 
    basics.info("Here, you will learn about the absolute basics of Python, like syntax, variables, and different data types. This is basics of Python.")
    basics.write("Python is probably the best programming language to start with, because it reads a lot like english, and can be used for a wide variety of things.")

    string_basics = basics.expander("Strings") 
    string_basics.write('''A string is anything surrounded in either (" "), or (' '). Go to the strings tab to learn more about strings and how they work.''')
    integers_basics = basics.expander("Integers")
    integers_basics.write('''An integer is a whole number, positive or negative, WITHOUT decimals.''')
    variables_basics = basics.expander("Variables")
    variables_basics.write('''A variable is a way to store information, like a container. You can put anything in there, and then use it later on in your code. For example, you could have a variable called `name` and store your name in there, and then use that variable to print your name later on.''')
    
    # --- Strings tab -----------------------

    strings.header("Strings")
    strings.write("Here is a simple example of Python code:")
    strings.code("print('Hello, World!')") 
    strings.write("Lets break down this code: "
    "`print()` is a function that outputs text to the console. "
    "`'Hello, World!'` is a string, represents text (normal writing). In this case, it will display the message 'Hello, World!' when the code is run.")
    strings.write("Notice how `'Hello, World!'` is surrounded by quotation marks? Thats how Python knows its not a variable or function, allowing you to write whatever you want in there without the console getting confused.")
   
   # The index = None is to make it so that the question isn't auto answered. Also, .radio is multiple choice questions.
    user_guess = strings.radio("Which option here is a string?", ["42", "hi!", "'Hello!'"], index = None, key = "quiz1")
    if user_guess: # This if statement is to make sure that the user has made a guess.
        if user_guess == "'Hello!'":
            strings.success("Yeah, 'Hello!' is a string because it is surrounded by quotation marks.")
        elif user_guess is not None: # if the answer is anything BUT the right answer, it will show this message.
            strings.error("Close. A string is a something that is surrounded by quotation marks.")
    st.divider() 
    

    user_guess2 = strings.radio("What are strings surrounded by?", ["brackets", "quotation marks", "parentheses", "Only the '' marks"], index = None, key = "quiz2")
    if user_guess2:
        if user_guess2 == "quotation marks":
            strings.success("Right! Strings are surrounded by quotations, which can be (' ') or (\" \")")
        elif user_guess2 is not None: 
            strings.error("While single quotation marks (' ') can be used to make strings, double ones (\" \") can also be used.") 
    # Didn't mention this earlier

    strings.subheader("Summary")
    strings.write("So, strings must be surrounded by quotations, and can have anything you want in there. They are used to represent text, like the ones your actually reading right now.")
    strings.write("If you want to have a string to actually appear where you want it to, for example the console, you would need to use the `print()` function. More on that later.")
    strings.write("Therefore, you can use strings for a variety of purposes, but its all up to you.")
    strings.code("print('Well done on completing your first lesson.')")
    
    # --- Integers tab ----------

    integers.header("Integers")
    integers.write("As you probably know, integers are whole numbers, positive or negative. They can be used for a bunch of things, like doing simple math, or even advanced math. However, unlike " \
    "strings, integers can't be used to represent text, and you probably shouldn't surround them in quotation marks." \
    "for example:")
    integers.code("print(42)")
    integers.write("This will print the number 42 to the console. However, if you put it in quotation marks, like this:")
    integers.code("print('42')")
    integers.write("It will print the string '42', which isn't a number.")
    
    # The key variable is so the program can easiler find everything.
    user_guess3 = integers.radio("Which one here is a integer?", ["42", "'42'", "Both of them"], index = None, key = "quiz3") 
    if user_guess3:
        if user_guess3 == "42":
            integers.success("Right! 42 is an integer because it is a whole number.")
        elif user_guess3 == "'42'":
            integers.error("Are you rushing or are you dragging?") 
        else:
            integers.error("not quite my tempo")
    
    integers.subheader("More things you can do with Integers")
    integers.write("As mentioned before, you can do math.")
    integers.code("print(2 + 2)") 
    integers.write("This will print 4, because 2 + 2 = 4.")
    integers.write("But thats just the start. But before you learn more, you'll need to know this:")
    different_math_things = { # This is the start of a table to show different math signs and what they do
        "Sign": ["`+`", "`-`", "`*`", "`/`", "`**`", "`%`"], # surrounded in `` because the console thought it was a list when I didn't want it to, so this is a easy fix.
        "Name": ["Addition", "Subtraction", "Multiplication", "Division", "Exponentiation", "Modulo"], # The names that will apear next to the signs
        "Purpose": [ 
            "Adding two numbers together",
            "Subtracting one number from another",
            "Multiplying two numbers together",
            "Dividing one number by another",
            "Raising a number to the power of another",
            "Finding the remainder after division"
        ],
        "example": [ 
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
    
    # --- Variables tab ---------------------

    variables.header("Variables")
    variables.write("Variables are what you store information in. You can put anything in there, and then use it later. For example, you could have \
                    a variable called `coolguy` and store the string 'Alex' in there, and then use that variable to print it later on.")
    variables.code("coolguy = 'Alex'\nprint(coolguy)") 
    variables.write("This will print 'Alex' to the console, because we stored that string in the variable `coolguy`. You can also store integers in variables, like this:")
    variables.code("age = 16\nprint(age)") # the \n just means go down a line or in some cases it makes a space.
    variables.write("This will print 16 to the console, because we stored that integer in the variable `age`. You can also do cool things in a variable, like this:")
    variables.code("alex_score = 17\nxavier_score = 20\nprint(alex_score + xavier_score)")
    variables.write("This will print 37 to the console, because we stored the integers 17 and 20 in the variables, and just added them together like boom.")


    container = variables.container(border = True) # creating a border around the container I made, so that its more aesthetically pleasing. Also has a copy and paste function. 
    container.subheader("Examples of variables")
    container.code("player_health = 1000\narmour_multiplier = 2\narmoured_health = player_health * armour multiplier\nprint(armoured_health)")
    container.write("**Console:** 2000") ## ** just means bold
    container.divider()
    container.code("best_sword = 'Katana'\nprint(best_sword)") 
    container.write("**Console:** Katana")
    container.code("sentence_start = 'You have'\nsentence_end = Health'\n\nplayer1_health = '1200'\nplayer2_health = '1100'\n\nprint(sentence_start + player1_health + sentence_end)\nprint(sentence_start + player2_health + sentence_end)")
    container.write("**Console:** You have 1200 Health.")
    container.write("**Console:** You have 1100 Health.")
    container.divider()
    container.write("Note: When making a variable with multiple words, you MUST use a _ (underscore) to connect those words, otherwise they will be counted as multiple different variables.") # Side note because I may have forgotten to mention it.