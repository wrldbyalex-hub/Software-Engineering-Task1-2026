import sqlite3
import hashlib
from datetime import datetime

DB_FILE = "users.db"

def init_db():
    """Initializes the database and creates the users table if it doesn't exist."""
    conn = sqlite3.connect(DB_FILE) # creates a connection to the database
    c = conn.cursor() # Creates a cursor object that runs the sql commands in c.execute for example 
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password_hash TEXT NOT NULL
        )
    """) # c.exucute just uses the cursor to create the data on the data table
    conn.commit() # saves it to the table 
    conn.close() # stops once completed 

def hash_password(password: str) -> str: # the arrow is the expected value 
    """Hashes a password using SHA256."""
    return hashlib.sha256(password.encode()).hexdigest() # hexdigest turns the encoded hashed passoword into a hexidecimal string

def check_credentials(username: str, password: str) -> bool:
    """Checks if username/password is correct."""
    conn = sqlite3.connect(DB_FILE) 
    c = conn.cursor()
    c.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
    result = c.fetchone() # Gets the next row of information 
    conn.close()
    if result:
        return result[0] == hash_password(password) # verifies the users password by comparing the password entered and the password saved
    return False

def user_exists(username: str) -> bool:
    """Checks if a username already exists."""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT 1 FROM users WHERE username = ?", (username,))
    exists = c.fetchone() is not None # stops duplicate accounts 
    conn.close()
    return exists

def create_user(username: str, password: str):
    """Creates a new user account."""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute(
        "INSERT INTO users (username, password_hash) VALUES (?, ?)",
        (username, hash_password(password))
    ) # Puts the new user details into the data table as a username and hashed password 
    conn.commit()
    conn.close()

# --- Questions ------------------------------------------

from datetime import datetime

def init_quiz_results_table():
    """Creates the quiz_results table if it doesn't exist."""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS quiz_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            timestamp TEXT NOT NULL,
            score INTEGER NOT NULL,
            total INTEGER NOT NULL,
            percentage REAL NOT NULL,
            FOREIGN KEY (username) REFERENCES users(username)
        )
    """)
    conn.commit()
    conn.close()

def save_quiz_result(username: str, score: int, total: int):
    """Saves the final quiz score to the database."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # the strftime converts the time taken by datetime.now and turns it into a string  
    percentage = round((score / total * 100), 1) if total > 0 else 0.0 # rounds it to one decimal place and makes sure that if its 0 it just skips to 0.0

    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""
        INSERT INTO quiz_results (username, timestamp, score, total, percentage)
        VALUES (?, ?, ?, ?, ?)
    """, (username, timestamp, score, total, percentage))
    conn.commit()
    conn.close()

def get_user_quiz_history(username: str, limit: int = 5):
    """Gets the most recent quiz results for the logged-in user."""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""
        SELECT timestamp, score, total, percentage 
        FROM quiz_results 
        WHERE username = ? 
        ORDER BY timestamp DESC 
        LIMIT ?
    """, (username, limit))
    results = c.fetchall() # grabs all of the most recent rows in the SQL using the cursor
    conn.close()
    return results # sends the results back to the function to be called on later 