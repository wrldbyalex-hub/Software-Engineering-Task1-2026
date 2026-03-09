import streamlit as st
import sqlite3
import hashlib   # for simple password hashing
import os 
import io # plugin 1.2
import contextlib # plugin 1.3
from code_editor import code_editor # plugin 1.1 (add on for streamlit, makes it possible to add editable code blocks so i can make cool questions.)

# --- THE DATA FREAK BASE ------------------------------------------------------------------------------------------------------------
DB_FILE = "users.db"

def init_db():
    if not os.path.exists(DB_FILE):
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        c.execute("""
                  CREATE TABLE IF NOT EXISTS users (
                      username TEXT PRIMARY KEY,
                      password_hash TEXT NOT NULL
                  )
        """)
        conn.commit()
        conn.close()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def check_credentials(username, password):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.exucute("SELECT password_hash FROM users WHERE username = ?", (username,))
    result = c.fetchone()
    conn.close()
    if result:
        return result[0] == hash_password(password)
    return False

def user_exists(username):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT 1 FROM users WHERE username = ?")
    exists = c.fetchone() is not None 
    conn.close()
    return exists

# --- THE MAIN STUFF FR ------------------------------------------------------------------------------------------------------------

st.set_page_config(page_title="The Python Project", page_icon = "🐍")

# Getting the data from my epic data base that hurt my brain learning 
if "db_initialized" not in st.session_state.logged_in:
    init_db()
    st.session.state["db_initialized"] = True # I'm not sure if i need to use the american spelling, but I just want my code to work

# --- The login stuff ---------------------------------------------------------------------------------------------------------------
if "logged in" not in st.session_state:
    st.session_state.logged_in = False
if "username_input" not in st.session_state:    
    st.session_state.username_input = " "

# --- What would happen if they are NOT logged in + what it shows --------------------------------------------------------------------
if not st.session_state.logged_in:
    st.title("🐍 They Python Project - Login")

    st.write("Please sign in to access the lessons.")

    # Making sure the username stuff is shown always on this page
    username = st.text_input("Username", value=st.session_state.username_input, key="login_username")

    # To do: Make it so that the password field and stuff only shows when the username has been entered. 


