# --- IMPORTS ---
from pages import basics, checkpoint, conclusion
from helpers import show_home_content

import streamlit as st
import sqlite3
import hashlib
import os

# --- DATABASE FILE ---
DB_FILE = "users.db"

# --- DATABASE SETUP ---
def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password_hash BLOB
        )
    """)
    conn.commit()
    conn.close()

# --- SECURITY ---
def hash_password(password):
    salt = os.urandom(16)
    hashed = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return salt + hashed

def check_password(stored_password, provided_password):
    salt = stored_password[:16]
    stored_hash = stored_password[16:]
    new_hash = hashlib.pbkdf2_hmac('sha256', provided_password.encode(), salt, 100000)
    return new_hash == stored_hash

# --- USER FUNCTIONS ---
def user_exists(username):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=?", (username,))
    result = c.fetchone()
    conn.close()
    return result is not None

def check_credentials(username, password):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT password_hash FROM users WHERE username=?", (username,))
    result = c.fetchone()
    conn.close()

    if result:
        return check_password(result[0], password)
    return False

# --- PAGE CONFIG ---
st.set_page_config(page_title="The Python Project", page_icon="🐍")

# --- SESSION STATE ---
if "db_initialized" not in st.session_state:
    init_db()
    st.session_state.db_initialized = True

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# --- LOGIN PAGE ---
if not st.session_state.logged_in:
    st.title("🐍 The Python Project - Login")
    st.write("Please sign in to access the lessons.")

    username = st.text_input("Username", key="login_username")
    password = st.text_input("Password", type="password", key="login_password")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Login", type="primary", use_container_width=True):
            if check_credentials(username.strip(), password):
                st.session_state.logged_in = True
                st.session_state.username = username.strip()
                st.rerun()
            else:
                st.error("Incorrect username or password :(")

    with col2:
        if st.button("Sign up", use_container_width=True):
            if not username.strip() or len(password) < 4:
                st.error("Username required & Password must be 4+ chars")
            elif user_exists(username.strip()):
                st.error("Username already taken.")
            else:
                conn = sqlite3.connect(DB_FILE)
                c = conn.cursor()
                c.execute(
                    "INSERT INTO users (username, password_hash) VALUES (?, ?)",
                    (username.strip(), hash_password(password))
                )
                conn.commit()
                conn.close()
                st.success("Account Created! Now you can log in.")

    st.info("Sign up if you're new here!")
    show_home_content()
    st.stop()

# --- MAIN APP ---
st.title("🐍 The Python Project")
st.write(f"Welcome, {st.session_state.get('username', 'Coder')}")

st.sidebar.title("Lessons")
st.sidebar.write(f"Logged in as: {st.session_state.username}")

the_page = st.sidebar.radio(
    "Go to:",
    ["Home Page", "The basics", "Check point", "Conclusion"]
)

# --- PROGRESS BAR ---
page_map = {"Home Page": 0, "The basics": 1, "Check point": 2, "Conclusion": 3}
current_step = page_map.get(the_page, 0)
total_steps = len(page_map) - 1

if current_step > 0:
    progress = current_step / total_steps
    st.sidebar.write(f"**Course Progress: {int(progress * 100)}%**")
    st.sidebar.progress(progress)
else:
    st.sidebar.progress(0.0)

# --- PAGE ROUTING ---
if the_page == "Home Page":
    show_home_content()

elif the_page == "The basics":
    basics.show()

elif the_page == "Check point":
    checkpoint.show()

elif the_page == "Conclusion":
    conclusion.show()

# --- LOGOUT ---
if st.sidebar.button("Logout"):
    st.session_state.clear()
    st.rerun()

# --- DEBUGGING NOTES ---
# Used print() and Streamlit outputs to track variable values
# Checked session_state to debug login issues
# Handled runtime errors using try/except blocks in checkpoint page