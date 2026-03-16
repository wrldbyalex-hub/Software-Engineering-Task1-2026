# --- IMPORTS ----------------------------------------------------------------------------------------------------------------
import streamlit as st
import sqlite3
import hashlib   
import os 
import io 
import contextlib 
from code_editor import code_editor 

# --- THE DATA BASE ------------------------------------------------------------------------------------------------------------
DB_FILE = "users.db" # name of the SQLite database file that will be created in the same folder

def init_db(): # Function that creates the database + table (only if they don't already exist)
    if not os.path.exists(DB_FILE): # check if the file users.db already exists
        conn = sqlite3.connect(DB_FILE) # create/connect to the database file (users.db)
        c = conn.cursor() # create a cursor  to run SQL commands
        c.execute("""
                  CREATE TABLE IF NOT EXISTS users (
                      username TEXT PRIMARY KEY,
                      password_hash TEXT NOT NULL
                  )
        """) # end of SQL
        conn.commit() # actually save (write) the changes
        conn.close() # Closes database connection 

def hash_password(password): # Converts password into fixed length hash
    return hashlib.sha256(password.encode()).hexdigest()
    # .encode() turns string into bytes 
    # sha256 creates 256 bit hash
    # .hexdigest() turns hash into hexadecimal string (hopefully)

def check_credentials(username, password): # Checks if the username and password that was entered is actually correct
    conn = sqlite3.connect(DB_FILE) # Creates a connection to data base
    c = conn.cursor() # creates a cursor for SQL
    c.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
    # ? Is a placeholder (shocker) to prevent SQL from touching it 
    result = c.fetchone() # Get the first thing that matches 
    conn.close() # Stop looking 
    if result: # If they found a match 
        return result[0] == hash_password(password) # Compare the stuff entered to the stuff in the data base 
    return False # if their isn't a user found they can't login 

def user_exists(username): # Check if the username is already being used 
    conn = sqlite3.connect(DB_FILE) 
    c = conn.cursor()
    c.execute("SELECT 1 FROM users WHERE username = ?", (username,))
    # We don't need actual data, select 1 is prettly light weight or whatever you call it
    exists = c.fetchone() is not None # If the row exists fetchone() returns the stuff (tuple (data structure and stuff)) but if its not None then it returns false.
    conn.close()
    return exists

# --- FUNCTION FOR HOME CONTENT ---------------------------------------------------------
def show_home_content(): 
    st.divider()
    st.markdown("## Why use python?")
    st.subheader("The popularity of the biggest languages (%)")
    st.write("The rest of the languages are not shown, but are the remaining 36% not shown on the cool graph.")

    chart_data_cool = {"Python": 25, "Java": 21, "JavaScript": 8, "C#": 7}
    st.bar_chart(chart_data_cool)

    st.markdown("Source: [statista]") # Credible source

    what_u_can_do, another_one = st.columns(2) # Looks nice and is a good way to sort information
    with what_u_can_do:
        st.subheader("What can you do with python?")
        st.image("https://f4.bcbits.com/img/a2712205983_16.jpg")
    with another_one:
        st.subheader("...a lot of stuff")
        st.write("Python is a very diverse language, allowing you to do a bunch of stuff:")
        st.markdown("- Web development\n- App development\n- Creating AI\n- Game development\n- Data Science\n- CyberSecurity\n- Robotics")
        st.markdown("and so much ***more***.")
        st.markdown('''
            :red[As you] :orange[can see,] :green[Python can] :blue[do some] :violet[really cool] 
            :gray[stuff as] :rainbow[shown above.]''') # The :colour in front is the colour that will appear on the words inside of the[]

# --- THE MAIN STUFF ----------------------------------------------------------------------------------------

st.set_page_config(page_title="The Python Project", page_icon="🐍")

# Initialize session state & db
if "db_initialized" not in st.session_state: # tells the console that it should check the data base to see if the user is logged in
    init_db()
    st.session_state["db_initialized"] = True 

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False 

# --- LOGGED OUT: show login + home content below it --------------
if not st.session_state.logged_in: # If the user isn't logged in it shows the login/sign up screen. 
    st.title("🐍 The Python Project - Login") 
    st.write("Please sign in to access the lessons.")

    # input fields to make sure they always show up
    username = st.text_input("Username", key="login_username")
    # text box for username, and key prevents the value reseting on return 
    password = st.text_input("Password", type="password", key="login_password")
    # The password field makes it appear as dots (type="password")

    # Creating columns for buttons
    col1, col2 = st.columns(2)        # Splits the screen into 2 different coloums 

    with col1:                  # The left coloum 
        if st.button("Login", type="primary", use_container_width=True):
            # Big button that fills the width of columns 
            if check_credentials(username.strip(), password):
                # strip() removes accidental spaces (like at the end or sum)
                st.session_state.logged_in = True # Changes the status of the user to logged in 
                st.session_state.username = username.strip() # remembers who logged in 
                st.rerun() # Forces streamlit to refresh the app 
            else:
                st.error("Incorrect username or password :(") # If they get that stuff wrong
    
    with col2:                          # Right column         
        if st.button("Sign up", use_container_width=True):
            if not username.strip() or len(password) < 4:
                st.error("Username required & Password must be 4+ chars")
                # Basic validation 
            elif user_exists(username.strip()):
                st.error("Username already taken.")
            else: 
                conn = sqlite3.connect(DB_FILE)
                c = conn.cursor()
                c.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)",
                           (username.strip(), hash_password(password)))
                # inserts a new user and saves the password as a hash (for the data base def at the top)
                conn.commit()                       # Saves it 
                conn.close()
                st.success("Account Created! Now you can log in.")
                # The account was created 

    st.info("Sign up if you're new here!")
    
    # Show the "Why use Python" content below the login box
    show_home_content()            # Calls on another function 
    st.stop()                   # Stops the exuction and makes it so the other parts of the app won't run unless the status is logged in.

# --- LOGGED IN: full experience with sidebar ---------------
st.title(f"🐍 The Python Project")
st.write(f"Welcome, {st.session_state.get('username', 'Coder')}")

st.sidebar.title("Lessons") 
the_page = st.sidebar.radio("Go to:", ["Home Page", "The basics", "Check point", "Conclusion"], key="nav_key") 

# --- PROGRESS BAR LOGIC -------------------------
page_map = {"Home Page": 0, "The basics": 1, "Check point": 2, "Conclusion": 3} 
current_step = page_map.get(the_page, 0)
total_steps = len(page_map) - 1 # minus 1 to get rid of home page 
# len grabs the amount of different variables (or strings in this case and turns it into a number) 
if current_step > 0: 
    progress_float = float(current_step / total_steps) # the len is then used here, allowing for more pages to be added and this code still working
    # Keep it between 0.0 and 1.0 so it doesn't crash
    super_progress_epic = max(0.0, min(progress_float, 1.0))
    st.sidebar.write(f"**Course Progress: {int(super_progress_epic * 100)}%**")
    st.sidebar.progress(super_progress_epic)
else: 
    st.sidebar.write("**Course Progress: 0%**")
    st.sidebar.progress(0.0)

# --- Pages ---------------------------------------------------------

if the_page == "Home Page":
    show_home_content()

elif the_page == "The basics":
    # Creates tabs for that page, all clickable
    basics, strings, integers, variables = st.tabs(["Basics", "Strings", "Integers", "Variables"]) #
    basics.header("Welcome to The Basics") 
    basics.info("Here, you will learn about the absolute basics of Python, like syntax, variables, and different data types. This is basics of Python.")
    basics.write("Python is probably the best programming language to start with, because it reads a lot like english, and can be used for a wide variety of things.")
    # expanders to make the page look nicer and less cluttered. They can also hold information, so that its more interactive. I like that.
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
    if user_guess: # This if statement is to make sure that the user has actually made a guess, and not just do nothing like a bum.
        if user_guess == "'Hello!'":
            strings.success("Yeah, 'Hello!' is a string because it is surrounded by quotation marks.")
        elif user_guess is not None: # if the answer is anything BUT the right answer, it will show this message. The reason I used elif instead of else is to make it so that if the user hasn't made a guess, it won't show the error message, because that would be annoying.
            strings.error("Close. A string is a something that is surrounded by quotation marks.")
    st.divider() 
    # divider to make the page look nicer and less cluttered.

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
    
    variables.header("Variables")
    variables.write("Variables are what you store information in. You can put anything in there, and then use it later. For example, you could have \
                    a variable called `coolguy` and store the string 'Alex' in there, and then use that variable to print it later on.")
    variables.code("coolguy = 'Alex'\nprint(coolguy)") # Explains pretty well how a variable works 
    variables.write("This will print 'Alex' to the console, because we stored that string in the variable `coolguy`. You can also store integers in variables, like this:")
    variables.code("age = 16\nprint(age)") # If you haven't picked up on this, the \n just means go down a line or in some cases it makes a space.
    variables.write("This will print 16 to the console, because we stored that integer in the variable `age`. You can also do cool things in a variable, like this:")
    variables.code("alex_score = 17\nxavier_score = 20\nprint(alex_score + xavier_score)")
    variables.write("This will print 37 to the console, because we stored the integers 17 and 20 in the variables, and just added them together like boom.")
    # Container to show a bunch of examples --------
    container = variables.container(border = True) # creating a border around the container I made, so that its more aesthetically pleasing. Also has a copy and paste function. 
    container.subheader("Examples of variables")
    container.code("player_health = 1000\narmour_multiplier = 2\narmoured_health = player_health * armour multiplier\nprint(armoured_health)")
    container.write("**Console:** 2000") ## ** just means bold
    container.divider()
    container.code("best_sword = 'Katana'\nprint(best_sword)") # Katanas are pretty cool
    container.write("**Console:** Katana")
    container.code("sentence_start = 'You have'\nsentence_end = Health'\n\nplayer1_health = '1200'\nplayer2_health = '1100'\n\nprint(sentence_start + player1_health + sentence_end)\nprint(sentence_start + player2_health + sentence_end)")
    container.write("**Console:** You have 1200 Health.") # Console result (if you were actually using a console what would appear)
    container.write("**Console:** You have 1100 Health.")
    container.divider()
    container.write("Note: When making a variable with multiple words, you MUST use a _ (underscore) to connect those words, otherwise they will be counted as multiple different variables.") # Side note because I may have forgotten to mention it.

# --- TEST --------------------------------------------------
elif the_page == "Check point":
        st.header("The Checkpoint")
        st.write("You've come far! Well done. But now is the time to put your knowledge to the test. Hopefully you get it all right, " \
        "and feel free to re-attempt any Questions, thats why they are still editable after getting it wrong/right.") # The slash above is so you don't have to scroll even further than you already are to read it, not as much for the website.
        st.caption("Sorry for the scrolling.")
        st.write("### How it works:")
        st.write("1. Read the question ")
        st.write("2. Write/click your answer")
        st.write("3. If its a console question (like the first one), when hovering over the final line of code, there will be a 'run' button on the side. Click that for your result. ")

        st.subheader("Question 1:")
        st.caption("Note: Don't worry if the brackets are highlighted red, that doesn't do anything.")
        st.write("The Game Fantasy Quest wants their variable enemy_type to equal 'monkey', but can't figure out why it won't print to the console. Use the space below to fix their code.") # Just a silly example fr

        btns = [{ # This is a list, with other things like true/false variables inside it, which is why its [{}] and not just []. btns is also short for buttons
            "name": "Run",
            "feather": "Play", #, just for a note, I wrote it this way because its easier to write all of this AND also is just easier to read and thus edit.
            "primary": True,
            "hasText": True,
            "commands": ["submit"],
            "style": {"bottom": "0.44rem", "right": "0.4rem"} # this is where the button will appear, so that the person can run the code. pretty Epic right?
        }]
    
        st.write("#### Task: Print the variable `enemy_type` to the console.") # ### makes it a header

        initial_code = "enemy_type = 'monkey'\n# Write your code below\n" # this is what will already be in the editor when the user opens up the page.
        response = code_editor(initial_code, lang = "python", buttons = btns) # code_editor is a plugin for streamlit, and is required for what I want to do.
                                        # lang just tells the code that this is python.
        if response['type'] == "submit": # if they submit the code that they entered with the below button
            user_code = response['text']
            output_buffer = io.StringIO() # calls on the streamlit again to save the code that they enter and use it later. 
            try: # the try statement allows the code to run even if it could result in a error, which is why I'm using it. 
                with contextlib.redirect_stdout(output_buffer): # Anything that would be written in the console will be put into the output buffer
                    exec(user_code, {}) # exec means execute, and then the {} is just the stuff from before
        
                printed_val = output_buffer.getvalue().strip() # output_buffer.getvalue sets apart some extra ram to catch everything the user is submitting. 
            # The .getvalue stores it and then pulls the result as one string, and the strip() removes all the empty space, like a space at the end of the code.
            # the printed_val is a new variable that can be assigned to whatever the user rights, but the if statement under detirmines if it is actually what we want.
                if printed_val == "monkey": # val is value, but i'm lazy when typing
                    st.success(f"Perfect! You printed: {printed_val}")
                elif printed_val == "": # if the code didn't actually print anything
                    st.warning("The code ran, but nothing was printed. Did you use print()?")
                else:
                    st.error(f"Almost! You printed '{printed_val}', but we expected 'monkey'.") 
            # Just adding that the expect fucntion is used with try, to stop the console from tweaking out that someone put in faulty code. 
            except Exception as e: # e just means error, so this will show if the code doesn't work, not if its just wrong. 
            # To add onto the except function, I'm using the universal (not a variable created by me) function called Exception which will, after its paused by except, send a missle at the code to destroy it. 
                st.error(f"Execution Error: {e}") # will tell them that the code exploded and died
        
            user_guess4 = st.radio("Question 2: Which here is a string?", ["'I'm so good at coding'", "I'm so good at coding", "(i'm so good at coding)"], index = None, key = "quiz4")
            if user_guess4: 
                if user_guess4 == "'I'm so good at coding'":
                    st.success("You are good at coding!")
                elif user_guess4 is not None:
                    st.error("You are kind of good at coding maybe?")

                user_guess5 = st.radio("Question 3: True or false; You can use the print() function to add numbers together.", ["True", "False"], index = None, key = "quiz5")
                if user_guess5:
                    if user_guess5 == "True": # If you look closly, you'll see that the each question is further indented into the code. This is to make it so that they appear AFTER the question is finished.
                        st.success("Correct! You can add numbers together. print(1 + 1) Would Print 2.") 
                    elif user_guess5 is not None:
                        st.error("Incorrect! Python can print numbers together, e.g print(5+2) would Print 7.")
                
                    user_guess6 = st.radio("Question 4: Which Symbol represents multiplication?", ["`x`", "`**`", "`*`", "`%`"], index = None, key = "quiz6")
                    if user_guess6:
                        if user_guess6 == "`*`":
                            st.success("Correct, in python the Multiplication symbol is *.")
                        elif user_guess6 == "`x`":
                            st.error("Good try, but thats a variable, not a symbol!")
                        elif user_guess6 == "`**`":
                            st.error("This is to the power of, not multiplication.")
                        elif user_guess6 == "`%`":
                            st.error("This is a symbol to find the remainder of a division question.")

                        st.subheader("Question 5:")
                        st.caption("Note: Don't worry if the brackets are highlighted red, that doesn't do anything.")
                        st.write("The Game Fantasy Quest has yet another problem! Make it so that their code can find the difference between Player1 score and Player2 score.")
                        initial_code2 = "player1_score = 2124\nplayer2_score = 1203\n# Write your code below\n" 
                        response2 = code_editor(initial_code2, lang = "python", buttons = btns) 
                                       
                        if response2['type'] == "submit": 
                            user_code2 = response2['text']
                            output_buffer2 = io.StringIO() # literally the same as question 1 
                            try:
                                with contextlib.redirect_stdout(output_buffer2): 
                                    exec(user_code2, {}) 
        
                                printed_val2 = output_buffer2.getvalue().strip() 
                                if printed_val2 == "921":
                                    st.success(f"Perfect! You printed: {printed_val2}")
                                elif printed_val2 == "":
                                    st.warning("The code ran, but nothing was printed. Did you use print()?")
                                else:
                                    st.error(f"Almost! You printed '{printed_val2}', but that isn't right.") 
                            except Exception as e2: 
                                st.error(f"Execution Error: {e2}") 
                            st.divider()
                            st.write("Well done. I know it wasn't that many quesstions, but these were simple enough to encompass what you learnt; Strings, variables and integers." \
                            "Remember, there is so, so much more. This is only the basics.")
elif the_page == "Conclusion":
    st.header("Goodbye")
    st.write("You have come quite a bit from 0 knowledge to this. I tried to make it so it was as simple as possible, and I hope I was able to do that for you.")
    st.write("But we're at the end now. You've finished the basics, but coding, Whether you think this is a good thing or not, coding never ends. There is always more you can learn- more you can do, and thats one of the beautiful things about it. ")
    st.write("Heres a little tease: F-strings. Functions. Syntax Errors. If you want to learn more, the first 3 chapters of a cool website called ***boot.dev*** will help you continue your learning path.")
    st.caption("You can always do it again though")
    st.subheader("Really cool button:")

    if "count" not in st.session_state: # if aren't there
        st.session_state.count = 0

    col1, col2, col3 = st.columns([1, 2, 1])   # middle column is wider

    with col1:
        pass  # empty left spacer

    with col2:
        left, mid, right = st.columns([1, 3, 1])   # extra centering inside

        with mid:
            if st.button("Click me! 🔥", use_container_width=True, type="primary"):
                st.session_state.count += 1 # += adds onto the total 

    with col3:
        if st.button("Reset"): # if the user for some reason wants to reset their useless number
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
    ) # HTML is rendered due to the unsafe_allow variable

    st.markdown(
        "<p style='text-align: center; color: #aaaaaa; font-size: 1.2rem; margin-top: -1rem;'>"
        "times clicked</p>",
        unsafe_allow_html=True
    )

    if st.session_state.count >= 100:
        st.write("what are you doing bro")
    
    if st.session_state.count>= 200:
        st.write("This isn't the point of the website bro")
# --- Log out ---------------------------------------------------------
if st.sidebar.button("Logout"):
    for key in list(st.session_state.keys()): # Finds the key that is currently being used
        del st.session_state[key] # deletes it do log them out 
    st.rerun() # Sends them back to the home page 
