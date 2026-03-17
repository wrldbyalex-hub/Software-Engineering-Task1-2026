# --- IMPORTS ----------------------------------------------------------------------------------------------------------------
import streamlit as st
import sqlite3
import hashlib
import os
import io
import contextlib
from code_editor import code_editor

# Import lesson pages 
import basics
import checkpoint
import conclusion
from utils import helpers, db  

# --- THE MAIN STUFF ----------------------------------------------------------------------------------------

st.set_page_config(page_title="The Python Project", page_icon="🐍")

# Initialize session state & db
if "db_initialized" not in st.session_state:
    db.init_db()
    st.session_state["db_initialized"] = True

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# --- LOGGED OUT: show login + home content below it --------------
if not st.session_state.logged_in:
    st.title("🐍 The Python Project - Login")
    st.write("Please sign in to access the lessons.")

    # input fields to make sure they always show up
    username = st.text_input("Username", key="login_username")
    password = st.text_input("Password", type="password", key="login_password")

    # Creating columns for buttons
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Login", type="primary", use_container_width=True):
            if db.check_credentials(username.strip(), password):
                st.session_state.logged_in = True
                st.session_state.username = username.strip()
                st.rerun()
            else:
                st.error("Incorrect username or password :(")

    with col2:
        if st.button("Sign up", use_container_width=True):
            if not username.strip() or len(password) < 4:
                st.error("Username required & Password must be 4+ chars")
            elif db.user_exists(username.strip()):
                st.error("Username already taken.")
            else:
                db.create_user(username.strip(), password)
                st.success("Account Created! Now you can log in.")

    st.info("Sign up if you're new here!")
    helpers.show_home_content()
    st.stop()

# --- LOGGED IN: full experience with sidebar ---------------
st.title(f"🐍 The Python Project")
st.write(f"Welcome, {st.session_state.get('username', 'Coder')}")

st.sidebar.title("Lessons")
the_page = st.sidebar.radio(
    "Go to:",
    ["Home Page", "The basics", "Check point", "Conclusion"],
    key="nav_key"
)

# --- PROGRESS BAR LOGIC -------------------------
page_map = {"Home Page": 0, "The basics": 1, "Check point": 2, "Conclusion": 3}
current_step = page_map.get(the_page, 0)
total_steps = len(page_map) - 1
st.sidebar.write(f"Logged in as: {st.session_state.username}")

if current_step > 0:
    progress_float = float(current_step / total_steps)
    super_progress_epic = max(0.0, min(progress_float, 1.0))
    st.sidebar.write(f"**Course Progress: {int(super_progress_epic * 100)}%**")
    st.sidebar.progress(super_progress_epic)
else:
    st.sidebar.write("**Course Progress: 0%**")
    st.sidebar.progress(0.0)

# --- Pages ---------------------------------------------------------
if the_page == "Home Page":
    helpers.show_home_content()
elif the_page == "The basics":
    basics.show()
elif the_page == "Check point":
    checkpoint.show()
elif the_page == "Conclusion":
    conclusion.show()

# --- Log out ---------------------------------------------------------
if st.sidebar.button("Logout"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()